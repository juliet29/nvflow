from cyclopts import App
import yaml
from plyze.qoi.data.data import convert_xarray_to_polars
import polars as pl

from plyze.qoi.data.interfaces import QOIandData
from plyze.qoi.registries.main import QOIRegistry

from nvflow.analysis_2.helpers import (
    read_csv_and_update_time_type,
    segment_wind_directions,
)
from nvflow.analysis_2.qoi_metrics import (
    plot_dimless_corr,
    plot_wind_dir_corr,
    prep_dfs,
)
from nvflow.constants import AmbientDataNames, Constants, RoomNames
from nvflow.paths import ProjectPaths
import altair as alt
from rich.pretty import pretty_repr
from plyze.flow_graph.create.main import make_flow_graph

import matplotlib.pyplot as plt
from loguru import logger
from utils4plans.logconfig import logset

from plyze.examples.casedata import example_casedata, example_times
from plyze.plots.altair_helpers import AltairRenderers
from plyze.plots.theme import default_theme

from nvflow.times import TimeSamples

app = App()


def keep():
    default_theme()
    logger.debug("")
    plt.plot()

    pretty_repr("")

    _ = example_casedata
    _ = example_times

    _ = make_flow_graph


### ------- START COMMANDS ---------


@app.command
def times():
    sql_path = ProjectPaths.more_eplus.sql
    wind_dirs = QOIandData(QOIRegistry.site.wind_direction, sql_path).original_arr
    df = (
        convert_xarray_to_polars(wind_dirs, "wind_direction")
        .sort(by="wind_direction")
        .with_columns(
            pl.col("wind_direction")
            .cut([10 * i for i in range(1, 37)], include_breaks=True)
            .alias("cut")
        )
        .unnest("cut")
        .group_by("breakpoint")
        .agg(
            [
                pl.col(Constants.DATETIME).first(),
                pl.col("category").first(),
                pl.col("wind_direction").first(),
            ]
        )
        .sort(by="breakpoint")
    )

    logger.info(
        f"first wind direction in 10º bins: {df.get_column("wind_direction").to_list()}"
    )

    datedf = (
        df.select(
            year=pl.col(Constants.DATETIME).dt.year(),
            month=pl.col(Constants.DATETIME).dt.month(),
            date=pl.col(Constants.DATETIME).dt.day(),
            hour=pl.col(Constants.DATETIME).dt.hour(),
        )
        .sort(by=["year", "month", "date", "hour"])
        .to_dict()
    )
    date_dict = {k: v.to_list() for k, v in datedf.items()}
    date_dict["year"] = date_dict["year"][0]
    date_dict["listwise"] = True  # pyright: ignore[reportArgumentType]

    dump_dict = {}
    dump_dict["time_selection"] = date_dict
    with open(ProjectPaths.config.wind_time_sel, "w") as yamlfile:
        data = yaml.dump(dump_dict, yamlfile)
    return date_dict


@app.command
def amb():
    ambient_path = ProjectPaths.sample_results.ambient
    df = read_csv_and_update_time_type(ambient_path)
    df = segment_wind_directions(df)
    return df.select(pl.col(AmbientDataNames.wind_group).value_counts())


@app.command
def fg():
    qoi_path = ProjectPaths.sample_results.qois
    metrics_path = ProjectPaths.sample_results.metrics
    ambient_path = ProjectPaths.sample_results.ambient

    dt = TimeSamples().single_time_noon
    room_name = RoomNames.room
    wind_group_start = 320
    # return prep_qoi_and_ambient(qoi_path, ambient_path, 320).select(
    #     pl.col(AmbientDataNames.wind_group)
    # )

    df = (
        prep_dfs(qoi_path, ambient_path, metrics_path, wind_group_start, room_name)
        .group_by(Constants.CASE)
        .agg(pl.col(pl.Float64).median())
    )
    # return df
    chart = plot_dimless_corr(df)
    chart.show()


@app.command
def gc():
    qoi_path = ProjectPaths.sample_results.qois
    metrics_path = ProjectPaths.sample_results.metrics
    ambient_path = ProjectPaths.sample_results.ambient

    dt = TimeSamples().single_time_noon
    room_name = RoomNames.room
    wind_group_start = 320
    # return prep_qoi_and_ambient(qoi_path, ambient_path, 320).select(
    #     pl.col(AmbientDataNames.wind_group)
    # )

    df = (
        prep_dfs(qoi_path, ambient_path, metrics_path, wind_group_start, room_name)
        .group_by([AmbientDataNames.wind_direction])
        .agg(pl.col(pl.Float64).median())
        .filter(pl.col(AmbientDataNames.wind_direction) > 330)
    )
    # return df
    # return df.select(pl.col(AmbientDataNames.wind_direction).value_counts())
    q = plot_wind_dir_corr(df, "zone_dimless_flow")
    t = plot_wind_dir_corr(df, "zone_dimless_temp")
    chart = q | t
    chart.show()


### ------- END COMMANDS ---------


def main():
    AltairRenderers.set_renderer()
    alt.theme.enable("default_theme")
    logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()

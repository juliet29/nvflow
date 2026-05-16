from pathlib import Path
from cyclopts import App
import yaml
from plyze.qoi.data.data import convert_xarray_to_polars
import polars as pl

from plyze.qoi.data.interfaces import QOIandData
from plyze.qoi.registries.main import QOIRegistry

from nvflow.constants import Constants

from loguru import logger


setup = App("setup")


def bin_df_by_wind_dir(df: pl.DataFrame):
    df = (
        df.sort(by="wind_direction")
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
    return df


def dump_time_selection_dict_to_yaml(df: pl.DataFrame, path: Path):
    datedf = (
        df.select(
            year=pl.col(Constants.DATETIME).dt.year(),
            month=pl.col(Constants.DATETIME).dt.month(),
            days=pl.col(Constants.DATETIME).dt.day(),
            hours=pl.col(Constants.DATETIME).dt.hour(),
        )
        .sort(by=["year", "month", "days", "hours"])
        .to_dict()
    )
    date_dict = {k: v.to_list() for k, v in datedf.items()}
    date_dict["year"] = date_dict["year"][0]
    date_dict["listwise"] = True  # pyright: ignore[reportArgumentType]

    dump_dict = {}
    dump_dict["time_selection"] = date_dict

    with open(path, "w") as yamlfile:
        _ = yaml.dump(dump_dict, yamlfile)

    return dump_dict


@setup.command
def gen_time_sel_yaml_for_wind_dir(sql_path: Path, yaml_path: Path):
    # sql_path = ProjectPaths.more_eplus.sql
    wind_dirs = QOIandData(QOIRegistry.site.wind_direction, sql_path).original_arr
    df = convert_xarray_to_polars(wind_dirs, "wind_direction").pipe(bin_df_by_wind_dir)

    logger.info(
        f"selected wind direction in 10º bins: {df.get_column("wind_direction").to_list()}"
    )

    dumped_dict = dump_time_selection_dict_to_yaml(df, yaml_path)

    return dumped_dict


# TODO: turn into a snakemake command, for now, its in a justfile..

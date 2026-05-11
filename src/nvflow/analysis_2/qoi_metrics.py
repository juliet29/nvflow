from functools import partial
from pathlib import Path

from loguru import logger
from plyze.metrics.registries import MetricRegistry
from nvflow.constants import AmbientDataNames, Constants, RoomNames
from plyze.flow_graph.interfaces import ZoneNodeQOINames
import polars as pl

from nvflow.analysis_2.helpers import (
    HandleWindDir,
    filter_rooms,
    read_csv_and_update_time_type,
    segment_wind_directions,
)


import altair as alt


def prep_qoi_and_ambient(
    qoi_path: Path,
    ambient_path: Path,
    wind_group_start: int,
):

    qoi_df = read_csv_and_update_time_type(qoi_path)
    ambient_df = (
        read_csv_and_update_time_type(ambient_path)
        .pipe(segment_wind_directions)
        .drop(Constants.SPACE)
    )

    join_df = ambient_df.join(qoi_df, on=Constants.DATETIME).filter(
        pl.col(AmbientDataNames.wind_group)
        == HandleWindDir.make_wind_group(wind_group_start)
    )
    logger.debug(join_df.select(pl.col(Constants.SPACE).value_counts()))

    return join_df


def prep_dfs(
    qoi_path: Path,
    ambient_path: Path,
    metrics_path: Path,
    wind_group_start: int,
    room_name: RoomNames,
):

    room_filter = partial(filter_rooms, room_name=room_name)
    qoi_ambient = prep_qoi_and_ambient(qoi_path, ambient_path, wind_group_start).pipe(
        room_filter
    )

    metrics_df = pl.read_csv(metrics_path)

    # join on case..
    join_df = metrics_df.join(qoi_ambient, on="case_name")
    return join_df


def plot_df(df: pl.DataFrame, metric: str, qoi: ZoneNodeQOINames):
    """metric should be a member of the plyze.metrics.registries MetricRegistry"""
    return (
        alt.Chart(df)
        .mark_point()
        .encode(x=alt.X(metric), y=alt.Y(qoi), color=alt.Color(Constants.CASE))
    )


def plot_dimless_corr(df: pl.DataFrame):
    FMR = MetricRegistry.flow
    PMR = MetricRegistry.plan
    metrics = [
        PMR.area,
        PMR.num_rooms,
        FMR.num_paths,
        FMR.degree_dom_node,
        FMR.avg_path_length,
        FMR.mode_path_length,
        FMR.len_shortest_path,
    ]
    metric_names = [i.name for i in metrics]

    def dim_qoi(qoi: ZoneNodeQOINames):
        chart = alt.HConcatChart()
        for m in metric_names:
            c = plot_df(df, m, qoi)
            chart |= c

        return chart

    q_chart = dim_qoi("zone_dimless_flow")
    temp_chart = dim_qoi("zone_dimless_temp")
    chart = q_chart & temp_chart
    return chart

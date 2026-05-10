from pathlib import Path
from nvflow.constants import Constants
from plyze.flow_graph.interfaces import ZoneNodeQOINames
import polars as pl
from datetime import datetime
from functools import partial

from nvflow.analysis_2.helpers import (
    filter_rooms,
    filter_time,
    read_csv_and_update_time_type,
)
from nvflow.constants import RoomNames


import altair as alt


def prep_dfs(
    qoi_path: Path, metrics_path: Path, dt: list[datetime], room_name: RoomNames
):
    time_filter = partial(filter_time, dt=dt)
    room_filter = partial(filter_rooms, room_name=room_name)

    qoi_df = read_csv_and_update_time_type(qoi_path).pipe(room_filter).pipe(time_filter)

    metrics_df = pl.read_csv(metrics_path)

    # join on case..
    join_df = metrics_df.join(qoi_df, on="case_name")
    return join_df


def plot_df(df: pl.DataFrame, metric: str, qoi: ZoneNodeQOINames):
    """metric should be a member of the plyze.metrics.registries MetricRegistry"""
    return (
        alt.Chart(df)
        .mark_point()
        .encode(x=alt.X(metric), y=alt.Y(qoi), color=alt.Color(Constants.CASE))
    )

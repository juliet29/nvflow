from plyze.flow_graph.interfaces import ZoneNodeQOINames
from datetime import datetime
import polars as pl
import altair as alt

from nvflow.analysis.constants import Constants
from nvflow.analysis.times import SampleTimes


# class RoomAtTime(pt.Model):
#     datetimes: pl.Datetime
#     case_name: str
#     space_names: str
#     mixing_volume: float
#     ventilation_volume: float
#     temperature: float
#


def collate_zone_data_dfs(case_names: list[str], dfs: list[pl.DataFrame]):
    new_dfs = [
        df.with_columns(pl.lit(case_name).alias(Constants.CASE))
        for df, case_name in zip(dfs, case_names)
    ]
    return pl.concat(new_dfs)


def get_data_at_time(df: pl.DataFrame, dt: list[datetime]):
    return df.filter(pl.col(Constants.DATETIME).is_in(dt))


def plot_hist(samples_df_at_time: pl.DataFrame, qoi: ZoneNodeQOINames):
    # sample a few cases -
    c = (
        alt.Chart(samples_df_at_time)
        .mark_bar()
        .encode(alt.X(qoi), y="count()", column=alt.Column(Constants.CASE))
    )
    return c


# case by case at time
def plot_case_by_case_for_qoi(sample_df: pl.DataFrame, qoi: ZoneNodeQOINames):
    def p(dt: list[datetime], name: str):
        df2 = get_data_at_time(sample_df, dt)
        return plot_hist(df2, qoi).properties(title=name)

    chart = alt.VConcatChart()
    for name, dt in SampleTimes().samples:
        c = p(dt, name)
        chart |= c

    return chart

from loguru import logger
from plyze.flow_graph.interfaces import ZoneNodeQOINames
from datetime import datetime
import polars as pl
import altair as alt

from nvflow.constants import Constants
from nvflow.times import create_time_samples


# class RoomAtTime(pt.Model):
#     datetimes: pl.Datetime
#     case_name: str
#     space_names: str
#     mixing_volume: float
#     ventilation_volume: float
#     temperature: float
#


def collate_zone_data_across_dfs(case_names: list[str], dfs: list[pl.DataFrame]):
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


def plot_hist_binned(
    samples_df_at_time: pl.DataFrame, qoi: ZoneNodeQOINames, step: float
):
    c = (
        alt.Chart(samples_df_at_time)
        .mark_bar()
        .encode(
            alt.X("binned_var", type="quantitative").title(f"{qoi}/S={step}"),
            y="count()",
            column=alt.Column(Constants.CASE),
        )
        .transform_bin("binned_var", field=qoi, bin=alt.BinParams(step=step))
    )
    return c


# case by case at time
def plot_case_by_case_for_qoi(
    sample_df: pl.DataFrame, qoi: ZoneNodeQOINames, step: float
):
    def p(dt: list[datetime], name: str):
        df2 = get_data_at_time(sample_df, dt).filter(pl.col(qoi) > 1)
        return plot_hist_binned(df2, qoi, step).properties(title=name)

    chart = alt.VConcatChart()
    for name, dt in create_time_samples():

        logger.debug((name, dt))

        c = p(dt, name)
        chart &= c

        # break

    return chart


def plot_case_by_case_for_qoi_env(
    sample_df: pl.DataFrame, qoi: ZoneNodeQOINames, step: float
):
    def p(dt: list[datetime], name: str):
        df2 = get_data_at_time(sample_df, dt).filter(pl.col(qoi) > 1)
        return plot_hist(df2, qoi).properties(title=name)

    chart = alt.VConcatChart()
    for name, dt in create_time_samples():

        logger.debug((name, dt))

        c = p(dt, name)
        chart &= c

        # break

    return chart

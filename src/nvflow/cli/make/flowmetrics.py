from datetime import datetime
from loguru import logger
import polars as pl
from typing import Annotated
from pathlib import Path
from cyclopts import App, Parameter
from plyze import FlowGraphModel, make_flow_graph, CaseData, make_metrics, MetricHolder


flowmetrics = App(name="flowmetrics")


@flowmetrics.command()
def create(
    idf_path: Path,
    sql_path: Path,
    dt: list[datetime],
    cardinal_expansion_factor: float,
    json_path: Path,
    data_path: Path,
):
    """
    Parameters
    ----------
    date_time: str
        Datetime format must be %Y-%m-%dT%H:%M:%S.
        See [cyclopts rules on coercing dates](https://cyclopts.readthedocs.io/en/latest/rules.html#datetime)
    """
    G = make_flow_graph(
        CaseData(idf_path, sql_path),
        cardinal_expansion_factor=cardinal_expansion_factor,
        dt=dt,
    )
    FlowGraphModel.write(G, json_path, data_path)
    logger.success("Finished writing graph")


@flowmetrics.command()
def create_metrics(json_path: Path, metrics_path: Path):
    G = FlowGraphModel.read(json_path)
    metrics = make_metrics(G)
    metrics.write(metrics_path)
    logger.success("Finished writing metrics")


@flowmetrics.command()
def consolidate(
    metrics_paths: Annotated[list[Path], Parameter(consume_multiple=True)],
    csv_path: Path,
):
    all_metrics = [MetricHolder.read(i) for i in metrics_paths]
    df = pl.DataFrame(all_metrics)
    df.write_csv(csv_path)
    logger.success("Finished consolidating JPG metrics")

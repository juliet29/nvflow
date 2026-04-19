from loguru import logger
import polars as pl
from typing import Annotated, NamedTuple
from pathlib import Path
from cyclopts import App, Parameter
from plyze import (
    FlowGraphModel,
    TimeSelection,
    make_flow_graph,
    CaseData,
    make_metrics,
    MetricHolder,
)


flowmetrics = App(name="flowmetrics")


@flowmetrics.command()
def create(
    idf_path: Path,
    sql_path: Path,
    ts: TimeSelection,
    cardinal_expansion_factor: float,
    json_path: Path,
    data_path: Path,
):
    datetimes = ts.calc_datetimes()
    G = make_flow_graph(
        CaseData(idf_path, sql_path),
        cardinal_expansion_factor=cardinal_expansion_factor,
        dt=datetimes,
    )
    FlowGraphModel.write(G, json_path, data_path)
    logger.success("Finished writing graph")


@flowmetrics.command()
def create_metrics(json_path: Path, metrics_path: Path):
    G = FlowGraphModel.read(json_path)
    metrics = make_metrics(G)
    metrics.write(metrics_path)
    logger.success("Finished writing metrics")


class MetricPathAndName(NamedTuple):
    path: Path
    name: str


@flowmetrics.command()
def consolidate(
    metrics_paths: Annotated[list[Path], Parameter(consume_multiple=True)],
    names: Annotated[list[str], Parameter(consume_multiple=True)],
    csv_path: Path,
):
    all_metrics = [
        {"case_name": name} | MetricHolder.read(path).holder_dict
        for (path, name) in zip(metrics_paths, names)
    ]
    df = pl.from_dicts(all_metrics)
    df.write_csv(csv_path)
    logger.success("Finished consolidating JPG metrics")

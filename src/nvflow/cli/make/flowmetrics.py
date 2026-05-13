from loguru import logger
from plyze.flow_graph.create.main import make_ambient_data
from plyze.qoi_flow_graph.zone_data import collate_ambient_data, collate_zone_data_to_df
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

from nvflow.constants import Constants


flowmetrics = App(name="flowmetrics")


class MetricPathAndName(NamedTuple):
    path: Path
    name: str


@flowmetrics.command()
def create(
    idf_path: Path,
    sql_path: Path,
    ts: TimeSelection,
    cardinal_expansion_factor: float,
    json_path: Path,
    data_folder_name: str,
):
    datetimes = ts.calc_datetimes()
    G = make_flow_graph(
        CaseData(idf_path, sql_path),
        cardinal_expansion_factor=cardinal_expansion_factor,
        dt=datetimes,
    )
    FlowGraphModel.write(G, json_path, data_folder_name)
    logger.success("Finished writing graph")


@flowmetrics.command()
def create_ambient_qois(sql_path: Path, ambient_data_path: Path, ts: TimeSelection):
    datetimes = ts.calc_datetimes()
    data = make_ambient_data(sql_path, datetimes)
    df = collate_ambient_data(data)
    df.write_csv(ambient_data_path)
    logger.success("Finished writing ambient data")


@flowmetrics.command()
def create_metrics(
    json_path: Path,
    metrics_path: Path,
):
    G = FlowGraphModel.read(json_path)
    metrics = make_metrics(G)
    metrics.write(metrics_path)
    logger.success("Finished writing metrics")


@flowmetrics.command()
def consolidate_metrics(
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
    logger.success("Finished consolidating metrics")


@flowmetrics.command()
def create_qois(
    json_path: Path,
    qoi_path: Path,
):
    G = FlowGraphModel.read(json_path)
    res = collate_zone_data_to_df(G)
    res.write_csv(qoi_path)
    logger.success("Finished writing qois")


@flowmetrics.command()
def consolidate_qois(
    qoi_paths: Annotated[list[Path], Parameter(consume_multiple=True)],
    names: Annotated[list[str], Parameter(consume_multiple=True)],
    csv_path: Path,
):
    def update_df(qoi_path: Path, name: str):
        return pl.read_csv(qoi_path).with_columns(pl.lit(name).alias(Constants.CASE))

    dfs = [update_df(qoi_path, name) for qoi_path, name in zip(qoi_paths, names)]
    df = pl.concat(dfs)

    df.write_csv(csv_path)
    logger.success("Finished consolidating qois")

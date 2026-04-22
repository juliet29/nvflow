from pathlib import Path

from nvflow.analysis.qoi_hist import collate_zone_data_dfs
from nvflow.paths import ProjectPaths
from plyze.qoi_flow_graph.zone_data import (
    collate_zone_data_to_df,
    extend_zone_data_df,
    make_enviro,
)
from plyze import FlowGraphModel


def prep_sample_graphs(paths: list[Path]):
    paths = ProjectPaths.sample_results.get_graph_jsons()
    assert paths[0].exists(), f"Can't find {paths[0]}"
    case_names = [i.parent.parent.name for i in paths]

    graphs = [FlowGraphModel.read(i) for i in paths]

    return graphs, case_names


def prep_basic_qois_df(paths: list[Path]):
    graphs, case_names = prep_sample_graphs(paths)

    dfs = [collate_zone_data_to_df(i) for i in graphs]
    sample_df = collate_zone_data_dfs(case_names, dfs)

    return sample_df


def prep_enviro_qois_df(paths: list[Path], sql: Path):
    graphs, case_names = prep_sample_graphs(paths)

    enviro = make_enviro(sql)
    dfs = [extend_zone_data_df(i, enviro) for i in graphs]
    sample_df = collate_zone_data_dfs(case_names, dfs)

    return sample_df

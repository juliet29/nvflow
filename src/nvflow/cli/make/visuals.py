from pathlib import Path
from cyclopts import App

from nvflow.analysis.metrics_hist import plot_metrics_histogram
from nvflow.analysis.qoi_hist import collate_zone_data_dfs
from nvflow.figure_utils import AltairChart, save_altair_figures
from nvflow.paths import ProjectPaths
from plyze.qoi_flow_graph.zone_data import collate_zone_data_to_df
from plyze import FlowGraphModel


visuals = App(name="visuals")


def handle_chart(
    c: AltairChart, save_path: Path, save: bool = False, stop_render: bool = False
):
    if not stop_render:
        c.show()
    if save:
        save_altair_figures(c, save_path)


@visuals.command
def plot_metrics(save: bool = False, stop_render: bool = False):
    c = plot_metrics_histogram(ProjectPaths.sample_results.metric_summary_csv)
    save_path = ProjectPaths.figures.design_metrics_corr_plot
    handle_chart(c, save_path, save, stop_render)


@visuals.command
def plot_qoi(save: bool = False, stop_render: bool = False):
    json_paths = ProjectPaths.sample_results.get_graph_jsons()
    case_names = [i.parent.parent.name for i in json_paths]

    graphs = [FlowGraphModel.read(i) for i in json_paths]
    dfs = [collate_zone_data_to_df(i) for i in graphs]
    sample_df = collate_zone_data_dfs(case_names, dfs)
    return sample_df

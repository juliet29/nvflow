from pathlib import Path
from cyclopts import App
from plyze.flow_graph.interfaces import ZoneNodeQOINames

# from plyze.qoi_flow_graph.zone_data import EnviroQOINames

from nvflow.analysis.metrics_hist import plot_metrics_histogram
from nvflow.analysis.qoi_helpers import prep_basic_qois_df
from nvflow.analysis.qoi_hist import (
    plot_case_by_case_for_qoi,
)
from nvflow.figure_utils import AltairChart, save_altair_figures
from nvflow.paths import ProjectPaths


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
    save_path = ProjectPaths.figures.design_metrics_histogram
    handle_chart(c, save_path, save, stop_render)


@visuals.command
def plot_qoi(
    qoi: ZoneNodeQOINames, save: bool = False, stop_render: bool = False, step=500
):
    sample_df = prep_basic_qois_df(ProjectPaths.sample_results.get_graph_jsons())

    # qoi: ZoneNodeQOINames = "ventilation_volume"
    c = plot_case_by_case_for_qoi(sample_df, qoi, step=step)

    save_path = ProjectPaths.figures.qoi_histogram / qoi
    handle_chart(c, save_path, save, stop_render)
    return sample_df


# @visuals.command
# def plot_qoi_env(
#     qoi: EnviroQOINames, save: bool = False, stop_render: bool = False, step=0.2
# ):
#     sample_df = prep_enviro_qois_df(
#         ProjectPaths.sample_results.get_graph_jsons(), ProjectPaths.eplus.sql
#     )
#
#     # qoi: EnviroQOINames = "temp_norm"
#     c = plot_case_by_case_for_qoi(sample_df, qoi, step=step)
#
#     save_path = ProjectPaths.figures.qoi_histogram / qoi
#     handle_chart(c, save_path, save, stop_render)
#     # return sample_df
#
#
# @visuals.command
# def make_plots():
#     # plot_qoi("mixing_volume", True, False)
#     # plot_qoi("ventilation_volume", True, False)
#     # plot_qoi("temperature", True, False, step=0.1)
#     plot_qoi_env("mix_norm", True, False, step=0.02)
#     plot_qoi_env("vent_norm", True, False, step=0.02)
#     plot_qoi_env("temp_norm", True, False, step=0.1)
#     plot_qoi_env("temp_norm_no_scale", True, False, 0.05)

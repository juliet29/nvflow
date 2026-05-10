from cyclopts import App

from nvflow.analysis_2.qoi_metrics import plot_df, prep_dfs
from nvflow.constants import RoomNames
from nvflow.paths import ProjectPaths
import altair as alt
from rich.pretty import pretty_repr
from plyze.flow_graph.create.main import make_flow_graph

import matplotlib.pyplot as plt
from loguru import logger
from utils4plans.logconfig import logset

from plyze.examples.casedata import example_casedata, example_times
from plyze.plots.altair_helpers import AltairRenderers
from plyze.plots.theme import default_theme

from nvflow.times import TimeSamples
from plyze.metrics.registries import MetricRegistry

app = App()


def keep():
    default_theme()
    logger.debug("")
    plt.plot()

    pretty_repr("")

    _ = example_casedata
    _ = example_times

    _ = make_flow_graph


### ------- START COMMANDS ---------


@app.command
def fg():
    qoi_path = ProjectPaths.sample_results.qois
    metrics_path = ProjectPaths.sample_results.metrics

    dt = TimeSamples().single_time_noon
    room_name = RoomNames.kitchen

    df = prep_dfs(qoi_path, metrics_path, dt, room_name)
    chart = plot_df(df, MetricRegistry.flow.degree_dom_node.name, "zone_dimless_flow")
    chart.show()


### ------- END COMMANDS ---------


def main():
    AltairRenderers.set_renderer()
    alt.theme.enable("default_theme")
    logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()

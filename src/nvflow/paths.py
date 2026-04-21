from pathlib import Path
import pyprojroot


BASE_PATH = pyprojroot.find_root(pyprojroot.has_dir(".git"))


class StaticPaths:
    base = Path(BASE_PATH) / "static"
    inputs = base / "1_inputs"
    temp = base / "4_temp"
    figures = base / "5_figures"


class SampleResults:
    base = StaticPaths.temp / "results"
    graphs_loc = base / "intermed"
    metric_summary_csv = base / "shared/flowmetrics/out.csv"

    @classmethod
    def get_graph_jsons(cls):
        return [i / "out.json" for i in cls.graphs_loc.iterdir()]


class FigureSaves:
    base = StaticPaths.figures
    design_metrics_corr_plot = base / "design_metrics_corr_plot"


class ProjectPaths:
    sample_results = SampleResults
    figures = FigureSaves

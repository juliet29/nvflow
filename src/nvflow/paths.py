from pathlib import Path
import pyprojroot


BASE_PATH = pyprojroot.find_root(pyprojroot.has_dir(".git"))


class StaticPaths:
    base = Path(BASE_PATH) / "static"
    inputs = base / "1_inputs"
    temp = base / "4_temp"
    figures = base / "5_figures"


class EplusSamples:
    base = StaticPaths.temp / "eplus_samples/1000"
    sql = base / "eplusout.sql"
    idf = base / "out.idf"


class SampleResults:
    base = StaticPaths.temp / "results"
    graphs_loc = base / "graphs"
    consolidated_data_loc = base / "cons"
    metrics = consolidated_data_loc / "metrics.csv"
    ambient = consolidated_data_loc / "ambient.csv"
    qois = consolidated_data_loc / "qois.csv"

    @classmethod
    def get_graph_jsons(cls):
        return [i / "out.json" for i in cls.graphs_loc.iterdir()]


class FigureSaves:
    base = StaticPaths.figures / "working"
    design_metrics_histogram = base / "design_metrics_histogram"
    qoi_histogram = base / "qoi_histogram"


class ProjectPaths:
    sample_results = SampleResults
    figures = FigureSaves
    eplus = EplusSamples

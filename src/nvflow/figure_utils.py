from pathlib import Path
from loguru import logger
from plyze.plots.theme import default_theme
import altair as alt
from utils4plans.io import create_time_string


# AltairChart = TypeVar("AltairChart", bound=alt.Chart)
AltairChart = (
    alt.Chart | alt.ConcatChart | alt.LayerChart | alt.HConcatChart | alt.VConcatChart
)


def keep():
    default_theme()


def save_altair_figures(figure: AltairChart, path: Path):
    default_theme()
    alt.theme.enable("default_theme")
    time = create_time_string()
    fig_name = f"{time}.png"

    save_path = path / fig_name

    save_path.parent.mkdir(parents=True, exist_ok=True)
    figure.save(save_path, format="png", scale_factor=1)
    logger.success(f"Saved figure to {save_path}")

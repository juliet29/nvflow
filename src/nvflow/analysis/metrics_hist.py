from pathlib import Path
import polars.selectors as cs
import polars as pl
import altair as alt


def plot_metrics_histogram(path: Path):
    df = pl.read_csv(path)

    metric_columns = df.select(~cs.starts_with("case"))

    chart = alt.VConcatChart()
    for metric in metric_columns.columns:
        source = df.select(metric)
        c = alt.Chart(source).mark_bar().encode(alt.X(metric).bin(), y="count()")
        chart &= c
    return chart

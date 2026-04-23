# !/bin/bash

SMKRUN="uv run snakemake \
  --cores 4  \
  --configfile=smkconfig/apptainer_run.yaml \
  --keep-going"

$SMKRUN graph_metrics_create_target
wait
#
$SMKRUN consolidate_target

# !/bin/bash

cd /nvflow
SMKRUN="uv run snakemake -c 1  --configfile=smkconfig/apptainer_test.yaml"

$SMKRUN graph_metrics_create_target
wait
#
$SMKRUN consolidate_target

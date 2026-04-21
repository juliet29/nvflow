# !/bin/bash
set -e

RESULTS_LOC="/nvflow/test"

cd /nvflow

rm -rf $RESULTS_LOC/*

SMKRUN="uv run snakemake -c 1  --configfile=smkconfig/apptainer_test.yaml"

$SMKRUN graph_metrics_create_target
wait
#
$SMKRUN consolidate_target

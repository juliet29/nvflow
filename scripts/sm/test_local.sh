# !/bin/bash
RESULTS_LOC="Users/julietnwagwuume-ezeoke/_UILCode/gqe-phd/fpopt/studies2/sherdirs/nvflow/static/4_temp/test"

rm -rf $RESULTS_LOC/*

SMKRUN="uv run snakemake -c 1  --configfile=smkconfig/local_test.yaml "

$SMKRUN graph_metrics_create_target
wait
#
$SMKRUN consolidate_target

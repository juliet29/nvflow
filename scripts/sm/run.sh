# !/bin/bash

set -e # exit on failure

cd /nvflow
SMKRUN="uv run snakemake -c 4  --configfile=smkconfig/apptainer_run_v0.yaml --keep-going"

# $SMKRUN grj
# wait
#
$SMKRUN consolidate_target

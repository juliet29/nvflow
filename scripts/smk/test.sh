#!/bin/bash

SMKRUN="uv run snakemake \
  --cores 1 \
  --configfile=smkconfig/apptainer_test.yaml"

$SMKRUN graph_metrics_create_target
wait
#
$SMKRUN consolidate_target

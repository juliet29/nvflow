#!/bin/bash

SMKRUN="uv run snakemake \
  --cores 1"
# --configfile=smkconfig/local_test.yaml"

$SMKRUN graphs_create_target
wait
#
$SMKRUN ambient_create_target
$SMKRUN metrics_create_target
$SMKRUN metrics_consolidate_target
$SMKRUN qois_consolidate_target

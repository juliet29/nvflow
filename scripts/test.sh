#!/bin/bash

# set -e

SMKRUN="uv run snakemake \
  --cores 1 \
  --keep-going \
  --configfile=smkconfig/wind_time_sel.yaml"

$SMKRUN graphs_create_target
wait
#

$SMKRUN plan_qois_create_target
$SMKRUN ambient_create_target
$SMKRUN metrics_create_target
$SMKRUN metrics_consolidate_target
$SMKRUN qois_consolidate_target

#!/bin/bash

set -e

SMKRUN="uv run snakemake \
  --cores 1 \
  --configfile=smkconfig/wind_dir_time_select.yaml"

$SMKRUN graphs_create_target
wait
#
$SMKRUN ambient_create_target
$SMKRUN metrics_create_target
$SMKRUN metrics_consolidate_target
$SMKRUN qois_consolidate_target

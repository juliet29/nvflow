#!/bin/bash
src_base="$SCRATCH/nvflow/run"
dest_base="$HOME/projects/nvflow/static/4_temp/results"

# Graphs
loc_src="$src_base/intermed"
loc_dest="$dest_base/intermed"
n_samples=10

set -e

echo "About to copy graphs to $loc_dest"
rm -rf $loc_dest/*
bash $HOME/scripts/copy_n_folders.sh $loc_src $loc_dest $n_samples

# Summaries
echo "About to copy summatry data to $loc_dest"
rm -rf $dest_base/shared/*
cp -r $src_base/shared $dest_base/shared

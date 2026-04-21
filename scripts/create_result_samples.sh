#!/bin/bash
src_base="$SCRATCH/nvflow/run"
dest_base="$HOME/projects/nvflow/static/4_temp/results"

# graphs
loc_src="$src_base/intermed"
loc_dest="$dest_base/intermed"
n_samples=10

# echo $loc_dest
# # rm -rf -I $loc_dest/*
# bash $HOME/scripts/copy_n_folders.sh $loc_src $loc_dest $n_samples

# summary data
rm -rf $dest_base/shared/*
cp -r $src_base/shared $dest_base/shared
#

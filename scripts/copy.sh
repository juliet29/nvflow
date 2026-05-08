#!/bin/bash

# Copies from OAK to local results

# TODO potentially ask for the time..
LOGIN="jnwagwu@login.sherlock.stanford.edu"
LATEST=$(ssh $LOGIN "ls -td $OAK/jnwagwu/nvflow/*/ | head -1")

DEST="/Users/julietnwagwuume-ezeoke/_UILCode/gqe-phd/fpopt/studies2/sherdirs/nvflow/static/4_temp/results"

rsync -avP --dry-run "$LOGIN:$LATEST/" "$DEST/"

echo "Proceed with copy? (press enter to continue)"
read status

rsync -avP "$LOGIN:$LATEST" "$DEST"

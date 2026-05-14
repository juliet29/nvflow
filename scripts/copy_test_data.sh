#!/bin/bash

# Copies from OAK to local results
LOCAL_OAK="/oak/stanford/groups/risheej"

LOGIN="jnwagwu@login.sherlock.stanford.edu"
LATEST="$LOCAL_OAK/jnwagwu/msherlock_v1/test_data/"

DEST="/Users/julietnwagwuume-ezeoke/_UILCode/gqe-phd/fpopt/studies2/sherdirs/nvflow/static/4_temp/more_eplus_samples/"

echo "SRC: $LATEST"
echo "DEST: $DEST"

rsync -avP --dry-run -e "ssh -q" "$LOGIN:$LATEST/" "$DEST/"

echo "Proceed with copy? (press enter to continue)"
read status

rsync -avP -e "ssh -q" "$LOGIN:$LATEST/" "$DEST/"

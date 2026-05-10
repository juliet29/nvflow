#!/bin/bash

# Copies from OAK to local results
LOCAL_OAK="/oak/stanford/groups/risheej"
# TODO potentially ask for the time..
LOGIN="jnwagwu@login.sherlock.stanford.edu"
LATEST="$LOCAL_OAK/jnwagwu/nvflow/$1"

DEST="/Users/julietnwagwuume-ezeoke/_UILCode/gqe-phd/fpopt/studies2/sherdirs/nvflow/static/4_temp/results"

echo "SRC: $LATEST"
echo "DEST: $DEST"

rsync -avP --dry-run -e "ssh -q" "$LOGIN:$LATEST/" "$DEST/"

echo "Proceed with copy? (press enter to continue)"
read status

rsync -avP -e "ssh -q" "$LOGIN:$LATEST/" "$DEST/"

#!/bin/bash
# move existing results to backup and make new folder
mv $SCRATCH/nvflow/test $SCRATCH/nvflow/test.$(date +%Y%m%d_%H%M%S).bak
mkdir -p $SCRATCH/nvflow/test/intermed
mkdir -p $SCRATCH/nvflow/test/shared
echo "moved test folder over"

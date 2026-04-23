#!/bin/bash

HOST_PROJECT="$HOME/projects/nvflow"
APPTAINER_PROJECT="/nvflow"
SAMPLES="$OAK/jnwagwu/msherlock_v1"
IMAGE="$HOST_PROJECT/apptainer/image.sif"

BINDS="--bind $HOST_PROJECT:$APPTAINER_PROJECT \
  --bind $SCRATCH/nvflow/run:/$APPTAINER_PROJECT/run \
  --bind $SCRATCH/nvflow/test:/$APPTAINER_PROJECT/test \
  --bind $SAMPLES/data:/$APPTAINER_PROJECT/samples/data \
  --bind $SAMPLES/test_data:/$APPTAINER_PROJECT/samples/test"

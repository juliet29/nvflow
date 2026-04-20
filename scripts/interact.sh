HOST_PROJECT="$HOME/projects/nvflow"
APPTAINER_PROJECT="/nvflow"
SAMPLES="$OAK/jnwagwu/msherlock_v1"

BINDS="--bind $HOST_PROJECT:$APPTAINER_PROJECT \
  --bind $SCRATCH/nvflow/run:/$APPTAINER_PROJECT/run \
  --bind $SCRATCH/nvflow/test:/$APPTAINER_PROJECT/test \
  --bind $SAMPLES/test_data:/$APPTAINER_PROJECT/samples/test \
  --bind $SAMPLES/data:/$APPTAINER_PROJECT/samples/data"

apptainer shell --pwd $APPTAINER_PROJECT $BINDS $HOST_PROJECT/apptainer/image.sif

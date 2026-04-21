#!/bin/bash
#SBATCH --job-name=nvflow
#SBATCH --output=/scratch/users/jnwagwu/submit/nvflow/%A/log.out
#SBATCH --error=/scratch/users/jnwagwu/submit/nvflow/%A/log.err
#SBATCH --partition=serc
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=4G
#SBATCH --time=3:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jnwagwu@stanford.edu

mkdir -p /scratch/users/jnwagwu/submit/nvflow

set -e

HOST_PROJECT="$HOME/projects/nvflow"
APPTAINER_PROJECT="/nvflow"
SAMPLES="$OAK/jnwagwu/msherlock_v1"
IMAGE="$HOST_PROJECT/apptainer/image.sif"

BINDS="--bind $HOST_PROJECT:$APPTAINER_PROJECT \
  --bind $SCRATCH/nvflow/run:/$APPTAINER_PROJECT/run \
  --bind $SCRATCH/nvflow/test:/$APPTAINER_PROJECT/test \
  --bind $SAMPLES/test_data:/$APPTAINER_PROJECT/samples/test \
  --bind $SAMPLES/data:/$APPTAINER_PROJECT/samples/data"

SMKRUN="uv run snakemake -c 4 --configfile=smkconfig/apptainer_run_v0.yaml --keep-going"

apptainer exec --pwd $APPTAINER_PROJECT $BINDS $IMAGE \
  bash -c "$SMKRUN graph_metrics_create_target && $SMKRUN consolidate_target"

#!/bin/bash
#SBATCH --job-name=nvflow_test
#SBATCH --output=/scratch/users/jnwagwu/submit/nvflow_test/%A/log.out
#SBATCH --error=/scratch/users/jnwagwu/submit/nvflow_test/%A/log.err
#SBATCH --partition=serc
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4G
#SBATCH --time=1:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jnwagwu@stanford.edu

mkdir -p /scratch/users/jnwagwu/submit/nvflow_test
PROJECT="$HOME/projects/nvflow"

set -e

source $PROJECT/scripts/apptainer_vars.sh

source $PROJECT/scripts/moves/test.sh

SCRIPT=$PROJECT/scripts/smk/test.sh
chmod +x $SCRIPT

apptainer exec --pwd $APPTAINER_PROJECT $BINDS $IMAGE $SCRIPT

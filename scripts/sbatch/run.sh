#!/bin/bash
#SBATCH --job-name=nvflow
#SBATCH --output=/scratch/users/jnwagwu/submit/nvflow/%A/log.out
#SBATCH --error=/scratch/users/jnwagwu/submit/nvflow/%A/log.err
#SBATCH --partition=serc

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4 # Should match the snakemake # of cores
#SBATCH --mem-per-cpu=4G
#SBATCH --time=3:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=jnwagwu@stanford.edu

mkdir -p /scratch/users/jnwagwu/submit/nvflow
PROJECT="$HOME/projects/nvflow/"

set -e

source $PROJECT/scripts/apptainer_vars.sh

source $PROJECT/scripts/moves/run.sh
wait

SCRIPT=$PROJECT/scripts/smk/run.sh
chmod +x $SCRIPT

apptainer exec --pwd $APPTAINER_PROJECT $BINDS $IMAGE $SCRIPT

source $PROJECT/scripts/create_result_samples.sh

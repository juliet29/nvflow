#!/bin/bash

source $HOME/projects/nvflow/scripts/apptainer_vars.sh

apptainer shell --pwd $APPTAINER_PROJECT $BINDS $HOST_PROJECT/apptainer/image.sif

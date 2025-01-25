#!/bin/bash

#SBATCH --job-name=18jan_main_overfit
#SBATCH --time=0-23:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --exclude=gpu-node[001-004]
#SBATCH --output=output.log
#SBATCH --error=error.log

# Purge all modules to avoid conflicts
module purge

# Load GPU drivers or other required modules if necessary
module load GpuModules

# Source Conda to enable the 'conda' command
source /home/g063292/miniconda3/etc/profile.d/conda.sh

# Activate your Conda environment
conda activate TextSummarization

# Force the script to use the Conda environment's Python explicitly
/home/g063292/miniconda3/envs/TextSummarization/bin/python --version  # Confirm Python version
/home/g063292/miniconda3/envs/TextSummarization/bin/python -c "import textSummarizer; print('textSummarizer is importable!')"
/home/g063292/miniconda3/envs/TextSummarization/bin/python main.py

#!/bin/bash
#SBATCH --time=5-00:00:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --partition=long
#SBATCH --output=output0.log
#SBATCH --error=error0.log


# Activate Conda environment
source ~/miniconda3/etc/profile.d/conda.sh  # Ensure Conda is available
conda activate TS

# Run the script
srun python "/work/ws-tmp/g063292-restore/g063292-projects-1736208608/Text_Summarization/Text_Summarization_Project/main.py"
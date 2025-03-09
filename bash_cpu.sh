#!/bin/bash
#SBATCH --time=5-00:00:00
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --partition=long
#SBATCH --output=output.log
#SBATCH --error=error.log

Conda activate TextSummarization

srun /work/ws-tmp/g063292-restore/g063292-projects-1736208608/Text _Summarization/Text_Summarization_Project/main.py
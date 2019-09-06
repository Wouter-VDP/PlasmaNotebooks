import glob 
import subprocess

for slurm in glob.glob('*.cmd'):
    print(slurm)
    res = subprocess.check_output(['sbatch', slurm])
    for line in res.splitlines():
        print(line)
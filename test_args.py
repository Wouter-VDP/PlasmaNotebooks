from plasma.conf_parser import parameters
import sys
conf_name = sys.argv[1]
conf = parameters("/home/wvdp/PPPLDeepLearning/slurm/MyConfigurations/" + conf_name + ".yaml")
print(conf)
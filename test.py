from plasma.conf_parser import parameters
from tensorflow.python.client import device_lib
import tensorflow as tf
import numpy as np
import os

print("Hello World")
print("\nNumpy version: ", np.__version__)
print("\nTensorflow version: ", tf.__version__)


def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']


print("\nList GPU devices availible: ")
get_available_gpus()
print(os.getcwd())

print("\nImport confiugurationfile: ")
conf = parameters("/home/wvdp/PPPLDeepLearning/slurm/MyConfigurations/conf_default.yaml")
print(conf)
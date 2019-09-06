from plasma.conf_parser import parameters
import os
import errno
import sys

conf_file = "/tmp/conf.yaml"
if os.path.exists(conf_file):
    conf = parameters(conf_file)
else:
    raise FileNotFoundError(
        errno.ENOENT, os.strerror(errno.ENOENT), 'conf.yaml')
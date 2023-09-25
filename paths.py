from inspect import getsourcefile
from os.path import abspath
import os, sys

# what = abspath(getsourcefile(lambda:0))

# print(what)

def get_current_dir():
  return os.path.dirname(os.path.abspath(sys.argv[0]))

def get_config_dir(filename=None):
  if filename is None:
    return get_current_dir() + "\\config\\"
  else:
    return get_current_dir() + "\\config\\" + filename + ".json"

def get_template_dir(filename=None):
  if filename is None:
    return get_current_dir() + "\\templates\\"
  else:
    return get_current_dir() + "\\templates\\" + filename + ".json"
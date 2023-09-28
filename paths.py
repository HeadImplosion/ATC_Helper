from inspect import getsourcefile
from os.path import abspath
from json_types import JsonTypes
import os, sys
import json

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

def get_paths_json():
  # Find directory of paths.json in config folder
  print("path: " + get_config_dir("paths"))

  file_config = open(get_config_dir("paths"))
  json_config_paths = json.load(file_config)
  json_dir = json_config_paths
  return json_dir

# Load ATC JSON files
def get_json_dir(json_type):
  json_dir = ""
  json_file = get_paths_json()

  # Get corresponding directory of AllTheCompressed JSONs
  match json_type:
    case JsonTypes.BLOCKSTATES:
      json_dir = json_file['paths']['create']['blockstates']
    case JsonTypes.MODELS_BLOCK:
      json_dir = json_file['paths']['create']['models']['block']
    case JsonTypes.MODELS_ITEM:
      json_dir = json_file['paths']['create']['models']['item']
    case JsonTypes.RECIPES_COMPRESS:
      json_dir = json_file['paths']['create']['recipes']['compress']
    case JsonTypes.RECIPES_DECOMPRESS:
      json_dir = json_file['paths']['create']['recipes']['decompress']
    case JsonTypes.ADVANCEMENTS_COMPRESS:
      json_dir = json_file['paths']['create']['advancements']['compress']
    case JsonTypes.ADVANCEMENTS_DECOMPRESS:
      json_dir = json_file['paths']['create']['advancements']['decompress']
    case JsonTypes.OVERLAY:
      json_dir = json_file['paths']['append']['overlay']
    case JsonTypes.LANG:
      json_dir = json_file['paths']['append']['lang']
    case _:
      json_dir = "invalid"

  return json_dir

print("Getting dir of 'blockstates': ")
print(get_json_dir(JsonTypes.BLOCKSTATES))
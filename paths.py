from inspect import getsourcefile
from os.path import abspath
from json_types import JsonTypes
import os, sys
import json
import traceback

# what = abspath(getsourcefile(lambda:0))

# print(what)

def get_current_dir():
  return os.path.dirname(os.path.abspath(sys.argv[0]))

def get_config_dir(filename=None):
  if filename is None:
    return get_current_dir() + "\\config\\"
  else:
    return get_current_dir() + "\\config\\" + filename + ".json"

def get_template_dir(json_type=None):
  try:
    template_filename = ""
    file_prefix = "template_"

    if json_type is not None:
      # JsonTypes.BLOCKSTATES.name.lower()

      template_filename = file_prefix + json_type.name.lower()

      return get_current_dir() + "\\templates\\" + template_filename + ".json"
    else:
      return get_current_dir() + "\\templates\\" + template_filename
  except:
    print("[paths.py:35]\tget_template_dir(json_type=None) ERROR! See below:")
    traceback.print_exc()
    return "_invalid"


def get_dirs_json():
  # Find directory of paths.json in config folder
  # print("path: " + get_config_dir("paths"))

  file_config = open(get_config_dir("paths"))
  return json.load(file_config)

# Load ATC JSON files
def get_json_dir(json_type):
  json_dir = ""
  json_file = get_dirs_json()

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

# print("Getting dir of 'blockstates': ")
# print("Blockstates dir: " + get_json_dir(JsonTypes.BLOCKSTATES))
# print("Block models dir: " + get_json_dir(JsonTypes.MODELS_BLOCK))
# print("Decompress recipes dir: " + get_json_dir(JsonTypes.RECIPES_DECOMPRESS))
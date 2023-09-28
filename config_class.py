from json_types import JsonTypes
import json
import paths

# Python directories
dir_current = paths.get_current_dir()
dir_config = paths.get_config_dir()
dir_template = paths.get_template_dir()

# Java (Minecraft) src directories
dir_java = "\\".join([dir_current, "java"])

def load_json_from_file(filename):
  dir_file_config = paths.get_config_dir(filename)
  file_config = open(dir_file_config, 'r')
  json_config = json.load(file_config)

  return json_config

# Retrieve list of all necessary file directories for mod
json_config = load_json_from_file("paths")

def get_local_file_dir(type):
  dir = ""
  json_root = json_config['paths']

  match type:
    case JsonTypes.BLOCKSTATES:
      return json_root['create']['blockstates']
    case JsonTypes.MODELS_BLOCK:
      return json_root['create']['models']['block']
    case JsonTypes.MODELS_ITEM:
      return json_root['create']['models']['item']
    case JsonTypes.RECIPES_COMPRESS:
      return json_root['create']['recipes']['compress']
    case JsonTypes.RECIPES_DECOMPRESS:
      return json_root['create']['recipes']['decompress']
    case JsonTypes.ADVANCEMENTS_COMPRESS:
      return json_root['create']['advancements']['compress']
    case JsonTypes.ADVANCEMENTS_DECOMPRESS:
      return json_root['create']['advancements']['decompress']
    case JsonTypes.OVERLAY:
      return json_root['append']['overlay']
    case JsonTypes.LANG:
      return json_root['append']['lang']
    case _:
      return ":)"
    

def get_full_dir(type):
  dir_local = get_local_file_dir(type)
  dir_full = dir_java + "\\" + dir_local
  
  return dir_full

# print(get_full_dir(JsonTypes.BLOCKSTATES))

# DEBUG
# decide_path1 = get_local_file_dir("overlay")
# print("Dir 1: " + decide_path1)
# decide_path2 = get_local_file_dir("models.item")
# print("Dir 2: " + decide_path2)

# print("Full dir: " + get_full_dir("blockstates"))
# print(get_local_file_dir(JsonTypes.BLOCKSTATES))
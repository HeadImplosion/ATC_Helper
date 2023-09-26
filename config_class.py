import json
import paths


def load_json_from_file(filename):
  dir_file_config = paths.get_config_dir(filename)
  file_config = open(dir_file_config, 'r')
  json_config = json.load(file_config)

  return json_config

# Python directories
dir_current = paths.get_current_dir()
dir_config = paths.get_config_dir()
dir_template = paths.get_template_dir()

# Java (Minecraft) src directories
dir_java = "\\".join([dir_current, "java"])

json_config = load_json_from_file("paths")

# print("blockstates path: " + load_json_from_file("blockstates"))
# print("models paths: " + load_json_from_file("models"))

def get_local_file_dir(type):
  dir = ""
  json_root = json_config['paths']

  match type:
    case "blockstates":
      return json_root['create']['blockstates']
    case "models.block":
      return json_root['create']['models']['block']
    case "models.item":
      return json_root['create']['models']['item']
    case "recipes.compress":
      return json_root['create']['recipes']['compress']
    case "recipes.decompress":
      return json_root['create']['recipes']['decompress']
    case "advancements.compress":
      return json_root['create']['advancements']['compress']
    case "advancements.decompress":
      return json_root['create']['advancements']['decompress']
    case "overlay":
      return json_root['append']['overlay']
    case "lang":
      return json_root['append']['lang']
    case _:
      return ":)"
    
# decide_path1 = get_local_file_dir("overlay")
# print("Dir 1: " + decide_path1)
# decide_path2 = get_local_file_dir("models.item")
# print("Dir 2: " + decide_path2)
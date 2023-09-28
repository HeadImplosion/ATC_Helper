import config_class
from enum import Enum
from json_types import JsonTypes

dir_current = config_class.dir_current
dir_config = config_class.dir_config
dir_template = config_class.dir_template
dir_java = config_class.dir_java

def ldir(dir_type):
  return config_class.get_local_file_dir(dir_type)

class JsonDirs(Enum):
  BLOCKSTATES = "\\".join([dir_java, ldir(JsonTypes.BLOCKSTATES)])
  MODELS_BLOCK = "\\".join([dir_java, ldir(JsonTypes.MODELS_BLOCK)])
  MODELS_ITEM = "\\".join([dir_java, ldir(JsonTypes.MODELS_ITEM)])
  RECIPES_COMPRESS = "\\".join([dir_java, ldir(JsonTypes.RECIPES_COMPRESS)])
  RECIPES_DECOMPRESS = "\\".join([dir_java, ldir(JsonTypes.RECIPES_DECOMPRESS)])
  ADVANCEMENTS_COMPRESS = "\\".join([dir_java, ldir(JsonTypes.ADVANCEMENTS_COMPRESS)])
  ADVANCEMENTS_DECOMPRESS = "\\".join([dir_java, ldir(JsonTypes.ADVANCEMENTS_DECOMPRESS)])
  OVERLAY = "\\".join([dir_java, ldir(JsonTypes.OVERLAY)])
  LANG = "\\".join([dir_java, ldir(JsonTypes.LANG)])
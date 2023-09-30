from enum import Enum

# Local src directories
# dir_local_blockstates = config_class.get_local_file_dir("blockstates")
# dir_local_models_block = config_class.get_local_file_dir("models.block")

# print(str(Directories.BLOCKSTATES.value))
# print(str(Directories.MODELS_BLOCK.value))
# print(str(Directories.MODELS_ITEM.value))
# print(str(Directories.RECIPES_COMPRESS.value))
# print(str(Directories.RECIPES_DECOMPRESS.value))
# print(str(Directories.ADVANCEMENTS_COMPRESS.value))
# print(str(Directories.ADVANCEMENTS_DECOMPRESS.value))

class JsonTypes(Enum):
  BLOCKSTATES = 1
  MODELS_BLOCK = 2
  MODELS_ITEM = 3
  RECIPES_COMPRESS = 4
  RECIPES_DECOMPRESS = 5
  ADVANCEMENTS_COMPRESS = 6
  ADVANCEMENTS_DECOMPRESS = 7
  OVERLAY = 8
  LANG = 9

  def get_layered_jsons():
    return [JsonTypes.RECIPES_COMPRESS, JsonTypes.RECIPES_DECOMPRESS,\
      JsonTypes.ADVANCEMENTS_COMPRESS, JsonTypes.ADVANCEMENTS_DECOMPRESS]
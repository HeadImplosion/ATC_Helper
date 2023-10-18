import json
import traceback
from block_class_local import BlockClassL
from json_types import JsonTypes
import paths

def read_lang_to_dict():
    
  dir_to_lang = paths.get_dir_from_atc_json_full(JsonTypes.LANG)
  # dir_to_lang = "C:\\Users\\MP\\Documents\\py\\AllTheCompressed\\src\\generated\\resources\\assets\\allthecompressed\\lang\\en_us.json"

  file_read_lang = open(dir_to_lang, 'r')
  dict_lang = json.load(file_read_lang)

  # print (dict_lang)
  # for e in dict_lang:
    # print("e: " + str(e))

  return dict_lang

# Create 1x - 9x entries for single block
def create_list_from_block(block: BlockClassL):
  build_list = list()
  for i in range(9):
    block_name_full = "".join(["block", ".allthecompressed.", block.block_name, "_", str(i+1), "x"])
    block_name_local = "".join([block.block_name_local, " ", str(i+1), "x"])
    build_pair = (block_name_full, block_name_local)
    build_list.append(build_pair)
  return build_list

# dict_lang: dict = read_lang_to_dict()
# list_block_local = create_list_from_block(BlockClassL("minecraft","azalea_planks", "Azalea Planks"))

def append_sort_dict(block: BlockClassL):
  list_from_dict_lang = list(read_lang_to_dict().items()) + create_list_from_block(block)
  list_from_dict_lang.sort()

  return dict(list_from_dict_lang)


# block_test = BlockClassL("minecraft", "water_source", "Water (Source)")

# with open('write_here.json','w') as outfile:
#   json.dump(append_sort_dict(block_test), outfile, indent=2)
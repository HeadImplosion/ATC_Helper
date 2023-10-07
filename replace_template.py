from block_class import BlockClass
from json_types import JsonTypes
import json
import paths
import re
import traceback

def replace_tag_template(line_array, block: BlockClass):
  user_input = block.block_name
  new_list = []
  print("Replacing [template] with user input...")
  for line in line_array:
    new_line = re.sub(r"\[template\]", user_input, line)
    new_list.append(new_line)
  return new_list

def replace_tag_no(line_array, index):
  new_list = []
  print("Replacing [no] with index...")
  for line in line_array:
    new_line = re.sub(r"\[no\]", str(index), line)
    new_list.append(new_line)
  return new_list

def replace_tag_mod(line_array, index):
  new_list = []
  print("Replacing [mod] with user input..")
  for line in line_array:
    new_line = re.sub(r"\[mod\]", str(index) + "x", line)
    new_list.append(new_line)
  return new_list

def replace_tag_no_x(line_array, index):
  new_list = []
  print("Replacing [no_x] with index_x...")
  for line in line_array:
    new_line = re.sub(r"\[no_x\]", str(index) + "x", line)
    new_list.append(new_line)
  return new_list

# #######
# # WIP #
# #######
# def replace_layered_json(json_type, input_block):
  
#   # json_types_layered = JsonTypes.get_layered_jsons()
  
#   dir_json = paths.get_template_dir(json_type)
#   file_json = open(dir_json, 'r')
#   json_loaded = json.load(file_json)
  
#   match json_type:
#     case JsonTypes.RECIPES_COMPRESS:
#       return write_compressed_recipe(json_type, input_block, json_loaded)
#     case JsonTypes.RECIPES_DECOMPRESS:
#       pass
#     case _:
#       return

# #######
# # WIP #
# #######
# def write_generic_json(json_type, block: BlockClass, json_loaded):
#   input_mod_name = block.mod_name
#   input_block_name = block.block_name

#   # Define JSON elements that need to be replaced.
#   # This depends on the JSON file being modified.

#   # Write 1x-9x block variants for specific JSON file

#   pass

# Format a single JSON string
def format_json_string(txt_json, block: BlockClass, index):
  txt_json_new = re.sub(r"\[template\]", block.block_name, txt_json)
  txt_json_new = re.sub(r"\[no_x\]", str(index + 1), txt_json_new)

  try:
    txt_json_new = re.sub(r"\[mod\]", block.mod_name, txt_json_new)
  except:
    print("format_json_string error: ")
    traceback.print_exc()
  
  return txt_json_new

#######
# WIP #
#######
def format_lesser_no_x(txt_json, index):


  # Compressed recipe JSONs have an extra step.
  # Change [lesser_no_x] depending on index in loop.
  txt_json_build = txt_json

  if index + 1 == 1:
    txt_json_build = re.sub(r"[\lesser_no_x\]", "", txt_json)
  else:
    txt_json_build = re.sub(r"\[lesser_no_x\]",\
      "".join(["_", str(index), "x"]), txt_json)
  return txt_json_build



def replace_lesser_no_x(line, index):
  str_index = str(index) + "x"
  if index == 1:
    str_index = ""
  return re.sub(r"\[lesser_no_x\]", str_index, line)

# replace_layered_json(JsonTypes.RECIPES_COMPRESS, BlockClass("minecraft", "believeblock"))


from block_class import BlockClass
from block_class_local import BlockClassL
import config_class
from json_dirs import JsonDirs
from json_types import JsonTypes
import copy
import json
import paths
import replace_template
import re
import traceback

# Create a blockstate file for user input
def write_blockstate(block: BlockClass, index):

  # Read template file for "blockstates" JSON (in templates folder)
  # Fill in template fields with user input
  template_filled_lines = replace_template_terms(\
    JsonTypes.BLOCKSTATES, block, index)

  # File is ready to be written.
  # Fetch directory for blockstates file
  # by joining directories (full current + local src)

  try:
    # Format file name to {name}_{n}x.json,
    # then write to corresponding directory
    # output_file = open(dir_output + user_input + "_" + str(index) + "x.json", 'w')
    dir_output = config_class.get_full_dir(JsonTypes.BLOCKSTATES)
    output_file = open("".join([dir_output + block.block_name, "_", str(index), "x.json"]), 'w')
    
    print("Writing to file: " +  dir_output + block.block_name + "_" + str(index) + "x.json")
    output_file.writelines(template_filled_lines)
    output_file.close()
    print("Successfully written blockstates file.")
  except FileNotFoundError as fe:
    print("ERROR: Directory does not exist: ")
    traceback.print_exc()
  except:
    print("ERROR: Unknown error occurred.")
  
  return

def template_file_to_strings(json_type):
  file_blockstates = open(paths.get_template_dir(json_type))
  file_blockstates.seek(0)
  txt_blockstates = file_blockstates.readlines()

  return txt_blockstates

def template_file_to_json(json_type):
  file_blockstates = open(paths.get_template_dir(json_type))
  file_blockstates.seek(0)
  json_blockstates = json.load(file_blockstates)
  return json_blockstates

def read_config(filename):
  path_file_config = paths.get_config_dir(filename)

  file_paths = open(path_file_config,"r")
  json_paths = json.load(file_paths)
  return json_paths

# Write 1x-9x variations of user input block
def write_blockstate_all(block: BlockClass):
  for x in range(9):
    print("Iteration no. " + str(x+1))
    write_blockstate(block, str(x+1))
  return

# Create a block model file from user input
def write_model_block(block: BlockClass, index):
  
  # Run lines array through replacement process twice
  template_filled_lines = replace_template_terms(\
    JsonTypes.MODELS_BLOCK, block, index)

  try:
    dir_output = config_class.get_full_dir(JsonTypes.MODELS_BLOCK)

    print("Writing block model file...")
    output_file = open("".join([\
      dir_output, block.block_name, "_", str(index), "x.json"]), 'w')
    output_file.writelines(template_filled_lines)
    output_file.close()

    print("Block model JSON written.")
  except FileNotFoundError:
    print("ERROR: Block model file cannot be written.")
  except:
    print("ERROR: Unknown error has occurred")

def write_model_block_all(block: BlockClass):
  for x in range(9):
    write_model_block(block, str(x+1))
  return

def write_model_item(block: BlockClass):
  # Get model/item/.json
  json_model_item = paths.get_json_template(JsonTypes.MODELS_ITEM)

  input_name_mod = block.mod_name
  input_name_block = block.block_name

  string_template_parent = json_model_item['parent']

  for i in range(9):
    def replace_parent(input_string):
      build_string = input_string
      build_string = re.sub(r"\[template\]", input_name_block, build_string)
      build_string = re.sub(r"\[no_x\]", str(i+1) + "x", build_string)
      return build_string

    built_string = replace_parent(string_template_parent)
    json_model_item['parent'] = built_string

    json_dir_model_item = paths.get_dir_from_atc_json_full(JsonTypes.MODELS_ITEM)
    write_to_file = "".join([json_dir_model_item, input_name_block, "_", str(i+1), "x.json"])
    try:
      with open(write_to_file, 'w') as outfile:
        json.dump(json_model_item, outfile, indent=2)
    except:
      pass

  print("hey")

def write_advancement_compress(block: BlockClass):
  # Get paths.json in config folder
  # and retrieve advancement/compress/.json path
  dir_adv_compress = paths.get_template_dir(JsonTypes.ADVANCEMENTS_COMPRESS)

  # Retrieve template_advancement_compress.json
  file_adv_compress = open(dir_adv_compress)
  array_str_adv_compress = file_adv_compress.readlines()

  # Replace [template]
  for i in range(9):
    array_build = []

    for line in array_str_adv_compress:
      # Replace [template]
      line_build = re.sub(r"\[template\]", block.block_name, line)
      line_build = re.sub(r"\[no_x\]", str(i+1) + "x", line_build)

      if i + 1 == 1:  # i.e. minecraft:[block]
        line_build = re.sub(r"\[mod\]", block.mod_name, line_build)
        line_build = re.sub(r"\[lesser_no_x\]", "", line_build)
      else:           # i.e. allthecompressed:[block]_1x to 8x
        line_build = re.sub(r"\[mod\]", "allthecompressed", line_build)
        line_build = re.sub(r"\[lesser_no_x\]", "".join(["_", str(i), "x"]), line_build)

      array_build.append(line_build)
    
    # Get write-to directory for compress advancement
    dir_to_adv_compress = paths.get_dir_from_atc_json_full(JsonTypes.ADVANCEMENTS_COMPRESS)
    write_to_file = "".join([dir_to_adv_compress, block.block_name, "_", str(i+1), "x.json"])
    # Re-write built lines into file
    try:

      with open(write_to_file, 'w') as outfile:
        outfile.writelines(array_build)
    except:
      print("Can't write advancement file: ")
      traceback.print_exc()

def write_advancement_decompress(block: BlockClass):
  # Get paths.json in config folder
  # and retrieve respective directory
  dir_adv_decompress = paths.get_template_dir(JsonTypes.ADVANCEMENTS_DECOMPRESS)

  # Retrieve template_adv_compress.json
  file_adv_decompress = open(dir_adv_decompress)
  array_str_adv_decompress = file_adv_decompress.readlines()

  for i in range(9):
    array_build = []

    for line in array_str_adv_decompress:
      line_build = re.sub(r"\[template\]", block.block_name, line)
      line_build = re.sub(r"\[no_x\]", str(i+1) + "x", line_build)
      array_build.append(line_build)
    
    dir_to_adv_decompress = paths.get_dir_from_atc_json_full(JsonTypes.ADVANCEMENTS_DECOMPRESS)
    write_to_file = "".join([dir_to_adv_decompress, block.block_name, "_", str(i+1), "x.json"])

    try:
      with open(write_to_file, 'w') as outfile:
        outfile.writelines(array_build)
    except:
      print("ERROR, can't write advancement file: ")
      traceback.print_exc()


# !!
def replace_template_terms(json_type, block: BlockClass, index):
  mod_name = "minecraft"

  # Fetch JSON object from file


  ## OUTDATED
  strings_template = template_file_to_strings(json_type)

  new_list = replace_template.replace_tag_template(strings_template, block)
  new_list = replace_template.replace_tag_no(new_list, str(index))

  # json_types_simple = [JsonTypes.BLOCKSTATES,\
  #   JsonTypes.MODELS_BLOCK, JsonTypes.MODELS_ITEM,\
  #   JsonTypes.OVERLAY, JsonTypes.LANG]
  json_types_layered = [\
    JsonTypes.RECIPES_COMPRESS, JsonTypes.RECIPES_DECOMPRESS,\
    JsonTypes.ADVANCEMENTS_COMPRESS, JsonTypes.ADVANCEMENTS_DECOMPRESS]

  match json_type:
    case json_type if json_type in json_types_layered:
      if (index > 1):
        mod_name = "allthecompressed"

  return new_list


# block_class.py:BlockClass
def write_compressed_recipe(block: BlockClass):

  # Load JSON file depending on JsonType
  json_c_recipe_template = paths.get_c_recipe_template()

  # GLOBAL
  # Use different replacement method
  input_name_mod = block.mod_name
  input_name_block = block.block_name

  # LOCAL
  # Get JSON elements to replace (2)
  txt_replace_key = json_c_recipe_template['key']['#']['item']
  txt_replace_result = json_c_recipe_template['result']['item']

  # Write all 9 variants of parent block
  for i in range(9):
  ###################
  # Local functions #
  ###################
    def replace_key(template_key):
      build_template_key = template_key

      build_template_key = re.sub(r"\[template\]", input_name_block, build_template_key)

      if i + 1 == 1:
        build_template_key = re.sub(r"\[mod\]", input_name_mod, build_template_key)
        build_template_key = re.sub(r"\[lesser_no_x\]", "", build_template_key)
      else:
        build_template_key = re.sub(r"\[mod\]", "allthecompressed", build_template_key)
        build_template_key = re.sub(r"\[lesser_no_x\]", "".join(["_", str(i), "x"]), build_template_key)
    
      return build_template_key
  
    def replace_result(template_result):
      build_template_result = template_result
      build_template_result = re.sub(r"\[template\]", input_name_block, txt_replace_result)
      build_template_result = re.sub(r"\[no_x\]", str(i+1) + "x", build_template_result)
      return build_template_result
  
  ###################
  ###################

  # Rebuild JSON
    json_c_recipe_template['key']['#']['item'] = replace_key(txt_replace_key)
    json_c_recipe_template['result']['item'] = replace_result(txt_replace_result)

  # Write to JSON file
    respective_json_dir = paths.get_dir_from_atc_json_full(JsonTypes.RECIPES_COMPRESS)
    write_to_file = "".join([respective_json_dir, input_name_block, "_", str(i+1), "x.json"])

    try:
      with open(write_to_file, 'w') as outfile:
        json.dump(json_c_recipe_template, outfile, indent=2)
    except:
      print("[replace_template.py] replace_layered_json() ERROR:")
      traceback.print_exc()

def write_decompressed_recipe(block: BlockClass):
  # Get JSON
  json_decompress_recipe = paths.get_json_template(JsonTypes.RECIPES_DECOMPRESS)

  input_name_mod = block.mod_name
  input_name_block = block.block_name

  # Get replaceable strings from said JSON
  string_template_ingredients = json_decompress_recipe['ingredients'][0]['item']
  string_template_result = json_decompress_recipe['result']['item']

  for i in range(9):
    # Replace ingredients.item
    # "item": "allthecompressed:[template]_[no_x]"
    def replace_item_ingredients(input_string):
      build_string = input_string
      build_string = re.sub(r"\[template\]", input_name_block, build_string)
      build_string = re.sub("\[no_x\]", str(i+1) + "x", build_string)
      return build_string
    
    # Replace result.item
    # "item": "[mod]:[template][lesser_no_x]"
    def replace_item_result(input_string):
      build_string = input_string
      build_string = re.sub(r"\[mod\]", input_name_mod, build_string)
      build_string = re.sub(r"\[template\]", input_name_block, build_string)

      if i + 1 == 1:
        build_string = re.sub(r"\[lesser_no_x\]", "", build_string)
      else:
        build_string = re.sub(r"\[lesser_no_x\]", "_" + str(i) + "x", build_string)

      return build_string
    
    replaced_ingredients = replace_item_ingredients(string_template_ingredients)
    replaced_result = replace_item_result(string_template_result)

    json_decompress_recipe['ingredients'][0]['item'] = replaced_ingredients
    json_decompress_recipe['result']['item'] = replaced_result

    json_dir_d_recipe = paths.get_dir_from_atc_json_full(JsonTypes.RECIPES_DECOMPRESS)
    write_to_file = "".join([json_dir_d_recipe, input_name_block, "_", str(i+1), "x.json"])      

    try:
      with open(write_to_file, 'w') as outfile:
        json.dump(json_decompress_recipe, outfile, indent=2)
    except:
      print("[write_files.py] write_decompressed_recipe() ERROR:")
      traceback.print_exc()
# dir_template_recipe_compress = "C:\\Users\\Zhad\\Documents\\atc\\templates\\template_recipes_compress.json"
# file = open(dir_template_recipe_compress, 'r')
# json_loaded = json.load(file)
# write_compressed_recipe(JsonTypes.RECIPES_COMPRESS,\
#   BlockClass("minecraft", "pootis"), json_loaded)

###############################
# Imported from external file #
###############################

def read_lang():
  # dir_to_lang = "en_us.json"
  dir_to_lang = paths.get_dir_from_atc_json_full(JsonTypes.LANG)

  file_read_lang = open(dir_to_lang, 'r')
  dict_lang = json.load(file_read_lang)

  return dict_lang

# Add both "block." and "item." tuples to list
def add_block_to_local_list(block: BlockClass):
  build_list = list()
  for i in range(9):
    # Tuple for block name and localized name
    block_name_full = "".join(["block", ".allthecompressed.", block.block_name, "_", str(i+1), "x"])
    item_name_full = "".join(["item", ".allthecompressed.", block.block_name, "_", str(i+1), "x"])
    block_name_local = "".join([block.block_name_local, " ", str(i+1), "x"])

    build_pair_block = (block_name_full, block_name_local)
    build_pair_item = (item_name_full, block_name_local)
    build_list.append(build_pair_block)
    build_list.append(build_pair_item)
  return build_list

# Compile all required blocks first.
def add_blocks_to_local_list(all_input_blocks: list[BlockClass]):
  build_list = []
  for block in all_input_blocks:
    build_list += add_block_to_local_list(block)

  return build_list

# Add to existing list
def append_existing_localization(block_list: list[BlockClass]):
  list_from_dict = list(read_lang().items())
  full_list = list_from_dict + block_list
  return full_list

# THEN sort
# Finally, convert back to dict
def list_to_sorted_dict(list):
  hold_list = list 
  hold_list.sort()
  pass
  return dict(hold_list)

def write_to_json(dict):
  with open(paths.get_dir_from_atc_json_full(JsonTypes.LANG), 'w') as outfile:
    json.dump(dict, outfile, indent=2)

def write_lang_from_block(local_block: BlockClassL):
  write_lang_from_blocks([local_block])
  pass

def write_lang_from_blocks(local_block_list: list):
  local_list_to_append = add_blocks_to_local_list(local_block_list)
  updated_list = append_existing_localization(local_list_to_append)
  dict_sorted = list_to_sorted_dict(updated_list)

  write_to_json(dict_sorted)

# ONE-TIME USE ONLY! 
def add_item_variant():
  # Open en_us.json file
  file_en_us = open('C:\\Users\\Zhad\\Documents\\atc\\java\\src\\generated\\resources\\assets\\allthecompressed\\lang\\en_us.json', 'r')
 
  json_en_us: dict = json.load(file_en_us)
  list_en_us_input = list(json_en_us.items())
  list_rebuild = copy.deepcopy(list_en_us_input)

  for i in list_en_us_input:
    # Read each of the key strings
    key_string = i[0]
    value_string = i[1]

    # Split key strings and rebuild with 'item'
    key_string_split: list = key_string.split('.')
    key_string_split[0] = "item"
    rebuilt_key_string = ".".join(key_string_split)

    rebuild_pair = (rebuilt_key_string, value_string)

    # Convert back to dict
    list_rebuild.append(rebuild_pair)

    print("Looping: " + str(i))
  # i.e.  block.allthecompressed.acacia_log
  #       -> ["block", "allthecompressed", "acacia_log"]
  pass
  dict_rebuilt = dict(list_rebuild)
  with open('TESTINGG.json', 'w') as outfile:
    json.dump(dict_rebuilt, outfile, indent=2)

# add_item_variant()

# block_input = BlockClassL.from_block(BlockClass("minecraft", "tinted_glass"), "Tinted Glass")
# block_input2 = BlockClassL.from_block(BlockClass("minecraft", "chiseled_glass"), "Chiseled Glass")
# block_input3 = BlockClassL.from_block(BlockClass("minecraft", "kyubey_remains"), "Kyubey Remains")

# block_list = [block_input, block_input2, block_input3]

# write_lang_from_blocks(block_list)

# pass

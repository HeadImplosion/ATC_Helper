from block_class import BlockClass
import config_class
from json_dirs import JsonDirs
from json_types import JsonTypes
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
def write_compressed_recipe(json_type, block: BlockClass, json_loaded):
  # GLOBAL
  # Use different replacement method
  input_mod_name = block.mod_name
  input_block_name = block.block_name

  # LOCAL
  # Get JSON elements to replace (2)
  txt_replace_key = json_loaded['key']['#']['item']
  txt_replace_result = json_loaded['result']['item']

  # Write all 9 variants of parent block
  for i in range(9):
  ###################
  # Local functions #
  ###################
    def replace_key(template_key):
      build_template_key = template_key

      build_template_key = re.sub(r"\[template\]", input_block_name, build_template_key)

      if i + 1 == 1:
        build_template_key = re.sub(r"\[mod\]", input_mod_name, build_template_key)
        build_template_key = re.sub(r"\[lesser_no_x\]", "", build_template_key)
      else:
        build_template_key = re.sub(r"\[mod\]", "allthecompressed", build_template_key)
        build_template_key = re.sub(r"\[lesser_no_x\]", "".join(["_", str(i), "x"]), build_template_key)
    
      return build_template_key
  
    def replace_result(template_result):
      build_template_result = template_result
      build_template_result = re.sub(r"\[template\]", input_block_name, txt_replace_result)
      build_template_result = re.sub(r"\[no_x\]", str(i+1) + "x", build_template_result)
      return build_template_result
  
  ###################
  ###################

  # Rebuild JSON
    json_loaded['key']['#']['item'] = replace_key(txt_replace_key)
    json_loaded['result']['item'] = replace_result(txt_replace_result)

  # Write to JSON file
    respective_json_dir = paths.get_json_dir_full(json_type)
    write_to_file = "".join([respective_json_dir, input_block_name, "_", str(i+1), "x.json"])

    try:
      with open(write_to_file, 'w') as outfile:
        json.dump(json_loaded, outfile, indent=2)
    except:
      print("[replace_template.py] replace_layered_json() ERROR:")
      traceback.print_exc()


dir_template_recipe_compress = "C:\\Users\\Zhad\\Documents\\atc\\templates\\template_recipes_compress.json"
file = open(dir_template_recipe_compress, 'r')
json_loaded = json.load(file)
write_compressed_recipe(JsonTypes.RECIPES_COMPRESS,\
  BlockClass("minecraft", "pootis"), json_loaded)
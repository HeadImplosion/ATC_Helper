from json_types import JsonTypes
import json
import paths
import re
import traceback

def replace_lines(line_array, user_input):
  new_list = []
  print("Replacing [template] with user input...")
  for line in line_array:
    new_line = re.sub(r"\[template\]", user_input, line)
    # print(new_line)
    new_list.append(new_line)
  return new_list

def replace_no(line_array, index):
  new_list = []
  print("Replacing [no] with index...")
  for line in line_array:
    new_line = re.sub(r"\[no\]", str(index), line)
    # print(new_line)
    new_list.append(new_line)
  return new_list

def replace_mod(line_array, index):
  new_list = []
  print("Replacing [mod] with user input..")
  for line in line_array:
    new_line = re.sub(r"\[mod\]", str(index) + "x", line)
    new_list.append(new_line)
  return new_list

def replace_no_x(line_array, index):
  new_list = []
  print("Replacing [no_x] with index_x...")
  for line in line_array:
    new_line = re.sub(r"\[no_x\]", str(index) + "x", line)
    new_list.append(new_line)
  return new_list

def replace_layered_json(json_type, input_mod_name, input_block):
  
  json_types_layered = [\
    JsonTypes.RECIPES_COMPRESS, JsonTypes.RECIPES_DECOMPRESS,\
    JsonTypes.ADVANCEMENTS_COMPRESS, JsonTypes.ADVANCEMENTS_DECOMPRESS]
  
  dir_json = paths.get_template_dir(json_type)
  file_json = open(dir_json, 'r')
  json_loaded = json.load(file_json)
  
  match json_type:
    # case json_type if json_type in json_types_layered:
    case JsonTypes.RECIPES_COMPRESS:
      # Use different replacement method
      block_id = ":".join([input_mod_name, input_block])

      # Get JSON elements to replace (2)
      txt_replace_key = json_loaded['key']['#']['item']
      txt_replace_result = json_loaded['result']['item']

      # Write all 9 variants of parent block
      for i in range(9):
        #Replace item element with parent block
        txt_replaced_key = re.sub(r"\[template\]", input_block, txt_replace_key)

        txt_replaced_result = re.sub(r"\[template\]", input_block, txt_replace_result)
        txt_replaced_result = re.sub(r"\[no\]", str(i+1), txt_replaced_result)

        if i + 1 == 1:
          txt_replaced_key = re.sub(r"\[mod\]", input_mod_name, txt_replaced_key)
          txt_replaced_key = re.sub(r"\[no_x\]", "", txt_replaced_key)
          pass
        else:
          txt_replaced_key = re.sub(r"\[mod\]", "allthecompressed", txt_replaced_key)
          txt_replaced_key = re.sub(r"\[no_x\]", "".join(["_", str(i), "x"]), txt_replaced_key)
          # Replace "item" element with ATC variant
        
        # Rebuild JSON
        json_loaded['key']['#']['item'] = txt_replaced_key
        json_loaded['result']['item'] = txt_replaced_result

        # Write to file
        #   i.  Get ATC JSON directory
        respective_json_dir = paths.get_json_dir_full(json_type)
        write_to_file = "".join([respective_json_dir, input_block, "_", str(i+1), "x.json"])

        #   ii. 
        try:
          with open(write_to_file, 'w') as outfile:
            json.dump(json_loaded, outfile, indent=2)
        except:
          print("[replace_template.py] replace_layered_json() ERROR:")
          traceback.print_exc()
          
      index = 0

      # Include x only if it's not the base (parent) block
      

      pass
    case _:
      # Use the usual replacement method
      pass

  # Open layered JSON
  # json_layered = json.load(file_json)
  # Select JSON elements to replace



  # Read JSON content

  # i.  If index is 1, keep input mod name and remove x suffix
  #     (i.e. minecraft:grass_block)
  #
  # ii. Otherwise, it becomes allthecompressed:[template]_[no_x]
  #     (i.e. allthecompressed:grass_block_1x)

  for index in range(9):
    if index + 1 == 1:
      pass
    else:
      pass

  # for line in line_array:
  #   if index == 1:
  #     new_line = re.sub(r"\[lesser_no_x\]", "", line)
  #     new_line = re.sub(r"\[mod\]", input_mod_name, new_line)
  #     new_line = re.sub(r"\[template\]", "", new_line)
  #   else:
  #     new_line = re.sub(r"\[lesser_no_x\]", str(index-1) + "x", line)

  # Get input mod name
  mod_name = "minecraft"
  # Get input block name
  block_name = "hee"

def replace_lesser_no_x(line, index):
  str_index = str(index) + "x"
  if index == 1:
    str_index = ""
  return re.sub(r"\[lesser_no_x\]", str_index, line)

replace_layered_json(JsonTypes.RECIPES_COMPRESS, "minecraft", "believeblock")
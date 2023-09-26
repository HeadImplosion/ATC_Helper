import replace_template
import json
import re
import paths
import config_class

# Create a blockstate file for user input
def write_blockstate(user_input, index):
  # Read template file for "blockstates" JSON (in templates folder)
  # Fill in template fields with user input
  template_filled_lines = replace_template_terms(\
    "template_blockstates", user_input, index)

  # File is ready to be written.
  # Fetch directory for blockstates file
  # by joining directories (full current + local src)

  try:
    # Format file name to {name}_{n}x.json,
    # then write to corresponding directory
    # output_file = open(dir_output + user_input + "_" + str(index) + "x.json", 'w')
    dir_output = get_full_dir("blockstates")
    output_file = open("".join([dir_output, user_input, "_", str(index), "x.json"]), 'w')
    
    print("Writing to file: " +  dir_output + user_input + "_" + str(index) + "x.json")
    output_file.writelines(template_filled_lines)
    output_file.close()
    print("Successfully written blockstates file.")
  except FileNotFoundError:
    print("ERROR: Directory does not exist.")
  except:
    print("ERROR: Unknown error occurred.")
  
  return

def template_file_to_strings(filename):
    file_blockstates = open(paths.get_template_dir(filename))
    file_blockstates.seek(0)
    txt_blockstates = file_blockstates.readlines()

    return txt_blockstates

def read_config(filename):
    path_file_config = paths.get_config_dir(filename)

    file_paths = open(path_file_config,"r")
    json_paths = json.load(file_paths)
    return json_paths

# Write 1x-9x variations of user input block
def write_blockstate_all(user_input):
  for x in range(9):
    print("Iteration no. " + str(x+1))
    write_blockstate(user_input, str(x+1))
  return

def get_full_dir(directory):
  dir_local = config_class.get_local_file_dir(directory)
  dir_output = "\\".join([config_class.dir_java, dir_local])
  return dir_output

# Create a block model file from user input
def write_model_block(user_input, index):
  
  # Run lines array through replacement process twice
  template_filled_lines = replace_template_terms(\
    "template_models_block", user_input, index)

  try:
    dir_output = get_full_dir("models.block")

    print("Writing block model file...")
    output_file = open("".join([\
      dir_output, user_input, "_", str(index), "x.json"]), 'w')
    output_file.writelines(template_filled_lines)
    output_file.close()

    print("Block model JSON written.")
  except FileNotFoundError:
    print("ERROR: Block model file cannot be written.")
  except:
    print("ERROR: Unknown error has occurred")

def write_model_block_all(user_input):
  for x in range(9):
    write_model_block(user_input, str(x+1))
  return

# # WIP!!!
# # Copy the above function and see if you can
# # create a generalized version for both blockstates and block model
# def write_file(user_input, index, template_name):
#   template_filled_lines = replace_template_terms(\
#     template_name, user_input, index)

def replace_template_terms(template_name, user_input, index):
  strings_template = template_file_to_strings(template_name)

  new_list = replace_template.replace_lines(strings_template, user_input)
  new_list = replace_template.replace_no(new_list, str(index))

  return new_list
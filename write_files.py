import replace_template
import json
import re
import paths
import config_class

# Create a file for a single compressed variant of input block
def write_blockstate(user_input, index=None):
  config_class.dir_config

  i = 1

  if index is not None:
    i = index

  # Retrieve list of directories for necessary files
  json_paths = read_config("paths")

  # Read blockstates template file
  strings_blockstates = template_file_to_strings("template_blockstates")

  # Replace [template] with user input, and store later
  new_list = replace_template.replace_lines(strings_blockstates, user_input)
  new_list2 = replace_template.replace_no(new_list, i)

  # Fetch directory for blockstates file
  dir_working = paths.get_current_dir()
  dir_blockstate = json_paths['paths']['create']['blockstates']
  dir_output = dir_working + "\\java\\" +  dir_blockstate

  print("blockstate: " + dir_working + dir_blockstate)
  # dir_output = paths.get_current_dir()

  try:
    print("DEBUG: " +  dir_output + user_input + "_" + str(i) + "x.json")
    output_file = open(dir_output + user_input + "_" + str(i) + "x.json", 'w')

    print("Writing to file...")
    output_file.writelines(new_list2)
    output_file.close()
  except FileNotFoundError:
    print("ERROR: Directory does not exist.")
  except:
    print("ERROR: Unknown error occurred.")
  
  return

def template_file_to_strings(filename):
    file_blockstates = open(paths.get_template_dir(filename))
    file_blockstates.seek(0)

    print("Store each line inside a list:")
    txt_blockstates = file_blockstates.readlines()
    return txt_blockstates

def read_config(filename):
    path_file_config = paths.get_config_dir(filename)

    file_paths = open(path_file_config,"r")
    json_paths = json.load(file_paths)
    return json_paths

# Write 1x-9x variations of user input block
def write_blockstate_all(user_input):
  count = 9
  for x in range(count):
    print("Iteration no. " + str(x+1))
    write_blockstate(user_input, str(x+1))
  return
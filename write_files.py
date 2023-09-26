import replace_template
import json
import re
import paths
import config_class

# Create a file for a single compressed variant of input block
def write_blockstate(user_input, index=None):
  config_class.dir_config
  i = -1

  if index is not None:
    i = index
  else:
    i = 1

  # Read template file for "blockstates" JSON (in templates folder)
  strings_blockstates = template_file_to_strings("template_blockstates")

  # Fill in template fields with user input
  new_list = replace_template.replace_lines(strings_blockstates, user_input)
  new_list = replace_template.replace_no(new_list, i)

  # File is ready to be written.
  # Fetch directory for blockstates file
  # by joining directories (full current + local src)
  dir_local_blockstates = config_class.get_local_file_dir("blockstates")
  dir_output = "\\".join([config_class.dir_java, dir_local_blockstates])

  try:
    # Format file name to {name}_{n}x.json,
    # then write to corresponding directory
    output_file = open(dir_output + user_input + "_" + str(i) + "x.json", 'w')

    print("Writing to file: " +  dir_output + user_input + "_" + str(i) + "x.json")
    output_file.writelines(new_list)
    output_file.close()
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
  count = 9
  for x in range(count):
    # print("Iteration no. " + str(x+1))
    write_blockstate(user_input, str(x+1))
  return
import replace_template
import json
import re
import paths

# Create a file for a single compressed variant of input block
def write_blockstate(user_input, index=None):
  i = 1

  if index is not None:
    i = index

  print("count is specified")
  # config_dir = paths.get_config_dir()
  file_config = paths.get_config_dir("paths")

  file_paths = open(file_config,"r")
  json_paths = json.load(file_paths)

  # 1. Read template file
  print("Load JSON file into variable")
  print("Set pointer to beginning of file")
  file_blockstates = open(paths.get_template_dir("template_blockstates"))
  file_blockstates.seek(0)

  print("Store each line inside a list:")
  txt_blockstates = file_blockstates.readlines()

  # Replace [template] with user input, and store later
  new_list = replace_template.replace_lines(txt_blockstates, user_input)
  new_list2 = replace_template.replace_no(new_list, i)

  # Write to file
  print("Creating file...")
  print("user_input: " + user_input)

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

# Write 1x-9x variations of user input block
def write_blockstate_all(user_input):
  count = 9
  for x in range(count):
    print("Iteration no. " + str(x+1))
    write_blockstate(user_input, str(x+1))
  return
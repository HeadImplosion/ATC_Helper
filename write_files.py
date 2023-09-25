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
  working_dir = paths.get_current_dir()
  config_dir = paths.get_config_dir()
  template_dir = paths.get_template_dir()
  file_paths = open(config_dir + "paths.json","r")

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
  output_file = open(user_input + "_" + str(i) + "x.json", 'w')

  print("Writing to file...")
  output_file.writelines(new_list2)
  output_file.close()
  
  return

# Write 1x-9x variations of user input block
def write_blockstate_all(user_input):
  count = 9
  for x in range(count):
    print("Iteration no. " + str(x+1))
    write_blockstate(user_input, str(x+1))
  return
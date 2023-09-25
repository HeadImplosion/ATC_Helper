import re
def replace_lines(line_array, user_input):
  new_list = []
  print("Replacing [template] with user input...")
  for line in line_array:
    new_line = re.sub(r"\[template\]", user_input, line)
    print(new_line)
    new_list.append(new_line)
  print("end of loop")
  return new_list

def replace_no(line_array, index):
  new_list = []
  print("Replacing [no] with index...")
  for line in line_array:
    new_line = re.sub(r"\[no\]", index, line)
    print(new_line)
    new_list.append(new_line)
  return new_list
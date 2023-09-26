import write_files
from my_class import myClass
import config_class

user_input = "testing"
# write_files.write_blockstate(user_input)
write_files.write_blockstate_all(user_input)
# write_files.write_blockstate_all("heh")
# write_files.write_blockstate_all("pootis")

print("LOOK HERE: " + config_class.get_local_file_dir("advancements.decompress"))
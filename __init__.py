from block_class import BlockClass
from mc_mods import McMods
import write_files
from my_class import myClass
import config_class

my_block = BlockClass(McMods.MINECRAFT.name.lower(), "vasi3")
user_input = "VASI2"
# write_files.write_blockstate(user_input)
write_files.write_blockstate_all(my_block)
write_files.write_model_block_all(my_block)

# print("LOOK HERE: " + config_class.get_local_file_dir("advancements.decompress"))
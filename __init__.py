from block_class import BlockClass
from mc_mods import McMods
import write_files
from my_class import myClass
import config_class
import traceback

def write_vanilla(block_name):
  mod_name = McMods.MINECRAFT.name.lower()
  block = BlockClass(mod_name, block_name)

  try:
    write_files.write_blockstate_all(block)
    write_files.write_model_block_all(block)
    write_files.write_model_item(block)
    write_files.write_compressed_recipe(block)
    write_files.write_decompressed_recipe(block)
    write_files.write_advancement_compress(block)
    write_files.write_advancement_decompress(block)

    print("Written all necessary files for block " + block_name + " succesfully.")
  except:
    print("ERROR occurred: ")
    traceback.print_exc()

# write_vanilla("oak_wood")

# write_vanilla("oak_wood")
# write_vanilla("acacia_wood")
# write_vanilla("birch_wood")
# write_vanilla("cherry_wood")
# write_vanilla("dark_oak_wood")
# write_vanilla("jungle_wood")
# write_vanilla("mangrove_wood")
# write_vanilla("spruce_wood")
# write_vanilla("crimson_hyphae")
# write_vanilla("warped_hyphae")
write_vanilla("iron_ore")

# write_files.write_advancement_compress(BlockClass("minecraft","horoscope"))
# write_files.write_advancement_decompress(BlockClass("minecraft","horoscope"))


# my_block = BlockClass(McMods.MINECRAFT.name.lower(), "wah")
# # user_input = "no"
# # write_files.write_blockstate(user_input)

# write_files.write_blockstate_all(my_block)
# write_files.write_model_block_all(my_block)
# write_files.write_model_item(my_block)
# write_files.write_compressed_recipe(my_block)
# write_files.write_decompressed_recipe(my_block)

# print("LOOK HERE: " + config_class.get_local_file_dir("advancements.decompress"))
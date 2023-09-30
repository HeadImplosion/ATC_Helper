from mc_mods import McMods

class BlockClass:
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, mod_name, block_name):
    self.mod_name = mod_name
    self.block_name = block_name

  def __repr__(self) -> str:
    return f"{type(self).__name__}(mod_name={self.mod_name}, block_name={self.block_name})"

  def get_block_id(self):
    return ":".join([self.mod_name, self.block_name])
  
tc = BlockClass(McMods.MINECRAFT.name.lower(), "believeblock")
print("Read: " + tc.mod_name)
print("Test: " + tc.get_block_id())
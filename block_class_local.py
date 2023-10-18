from block_class import BlockClass

class BlockClassL(BlockClass):
  def __init__(self, mod_name, block_name, block_name_local):
    super().__init__(mod_name, block_name)
    self.block_name_local = block_name_local

  @classmethod
  def from_block(cls, block: BlockClass, local_name):
    block_l = cls(block.mod_name, block.block_name, local_name)
    # Return class
    return block_l
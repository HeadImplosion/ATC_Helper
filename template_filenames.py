from enum import Enum

prefix = "template_"

def format_filename(filename):
  return "".join([prefix, filename, ".json"])

class TemplateNames(Enum):
  BLOCKSTATES = format_filename("blockstates")
  MODELS_BLOCK = format_filename("models_block")
  MODELS_ITEM = format_filename("models_item")
  RECIPES_COMPRESS = format_filename("recipes_compress")
  RECIPES_DECOMPRESS = format_filename("recipes_decompress")
  ADVANCEMENTS_COMPRESS = format_filename("advancements_compress")
  ADVANCEMENTS_DECOMPRESS = format_filename("advancements_decompress")
  OVERLAY = format_filename("overlay")
  LANG = format_filename("lang")
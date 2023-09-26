import json
import paths

working_dir = paths.get_current_dir()
config_dir = paths.get_config_dir()
template_dir = paths.get_template_dir()

file_paths = open(config_dir + "paths.json","r")
data = json.load(file_paths)
path_blockstates = data['paths']['create']['blockstates']
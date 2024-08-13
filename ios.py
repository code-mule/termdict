# bertrandterrier@codeberg.org/termdict/ios.py

import os
import shutil
import toml

# Create necessary paths
fdir:str = os.path.dirname(os.path.abspath(__file__))
tmpl_conf_path:str = os.path.join(fdir,"tmpl/config.toml") 
conf_dir:str = os.path.expanduser("~/.termdict")
conf_path:str = os.path.join(conf_dir,"config.toml")

# ================================================== #

def first_time() -> None:
    if not os.path.exists(conf_dir):

        # Create configuration directory
        os.mkdir(os.path.expanduser("~/.termdict"))

        # Create configuration file
        shutil.copy2(tmpl_conf_path,conf_path)

    return

class ConfigSettings:

    def __init__(self): 
        self.content:dict = self.load_config()
        self.settings:list = [key for key in self.content.keys()]

    def load_config(self):
        print('--Reading file')
        print(f'\t ::{conf_path}')
        
        with open(conf_path,'r') as f:
            configs:dict = toml.load(f)
    
        print('== Loaded configurations.')

        return configs

    def get_val(self,conf_key):
        if not conf_key in self.settings:
            print(f'== WARNING.\n\t::No setting like\n\t > {conf_key}')
            return
        
        return self.content[conf_key]
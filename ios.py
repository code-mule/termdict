# bertrandterrier@codeberg.org/termdict/ios.py

import os
import shutil

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
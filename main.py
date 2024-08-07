# bertrandterrier@codeberg.org/termdict/main.py

from ios import first_time
from com import get_cl_args
import pandas as pd
import sys

# ================================================== #

def preprocess(
        conf:bool,
        legend:bool,
        new:str|None,
        sec:bool
) -> int:
    if conf == True:
        ### CONFIGURATION ###
        return 1
    
    if legend == True:
        pass

    if new == True:
        ### CREATE NEW TABLE ###
        pass

    return 0

class TermDict:

    def __init__(
            self,
            csv:str,
            data:str,
            tbl_style:str,
            new:bool
            ) -> int:
        self.df = pd.read_csv(csv)
        self.cols = self.df.columns


def main():
    # Create configuration directory if not existing
    first_time()

    # Get arguments
    args = get_cl_args()

    # preprocess
    rt_code:int = preprocess(conf=args.config,
                             legend=args.legend,
                             new=args.new,
                             sec=args.secondary
                             )
    if rt_code >= 1:
        # !!! CONFIGURATION SETTINGS FUNCTION !!! #
        sys.exit(1)
    
    # Initialize dictionary object
    return

if __name__ == "__main__":
    main()
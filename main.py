# bertrandterrier@codeberg.org/termdict/main.py

from ios import first_time
from com import get_cl_args
import pandas as pd
import sys
from tabulate import tabulate

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
            data_dir:str,
            tbl_style:str,
            new:bool,
            highlight_col:dict,
            highlight_dict
            ) -> int:
        # Colors
        self.MAGENTA = '\033[5m'
        self.CYAN = '\033[6m'
        self.YELLOW = '\033[3m'

        # Data
        self.df = pd.read_csv(csv)
        self.cols = self.df.columns
        self.hl_cols = highlight_col
        self.hl_dict = highlight_dict

        # Create table from pandas DataFrame
        self.tbl:str = self.create_term_tbl(tbl_style,highlight_cols)

    def create_term_tbl(self,style) -> str:
        tabel:str = tabulate(tabular_data=self.df,
                                headers='keys',
                                TableFormat=style
                                )
        tmp_df:pd.DataFrame = self.df.copy()

        col_row = {
            0 : [],
            1 : [],
            2 : []
        }
        

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
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
            highlight_cols:dict
            ) -> int:
        # Colors
        self.MAGENTA = '\033[5m'
        self.CYAN = '\033[6m'
        self.ORANGE = '\033[3m'
        self.RESET = '\033[0m'
        self.RESET = '\033[1m'

        # Data
        self.df = pd.read_csv(csv)
        self.cols = self.df.columns
        self.hl_cols = highlight_cols

        # Create table from pandas DataFrame
        self.tbl:str = self.create_term_tbl(tbl_style)

        # Create the menu legend
        self.menu:dict = {
            '+':'Add entry',
            '-':'Delete entry',
            'i':'Inspect entry. (i;<entry-idx>)',
            'f':'Find entry. (f:<column>)',
            'st':'Show top (st:<range>, default=10)',
            'sb':'Show from bottom (sb:<range>,default=10)',
            'w':'Save changes.',
            'q':'Quit, (`wq`: Save and quit.)',
            '<command>!':'Enforce command.',
            '?':'Show legend.'
        }

    def create_term_tbl(self,style:str,rng:tuple=(-1,-1)) -> str:
        """Creates a graphical string for table output.

        Args:
            style (str): Style for the graphical representation of the tabulate function.

        Returns:
            str: The table, set and colorized.
        """
        if rng == (-1,-1):
            tmp_df:pd.DataFrame = self.df.copy()
        elif rng[0] == -1:
            tmp_df:pd.DataFrame = self.df.iloc[:rng[1],:].copy()
        elif rng[1] == -1:
            tmp_df:pd.DataFrame = self.df.iloc[rng[0]:,:].copy()
        else:
            tmp_df:pd.DataFrame = self.df.iloc[rng[0]:rng[1],:].copy()
        

        for col,idx in self.hl_cols.items():
            if col not in tmp_df[col]:
                print(
                    '==> WARNING.'
                    f'Column {col} not in DataFrame'
                )
                continue

            if tmp_df[col].dtypes in ['int64','float64']:
                tmp_df[col] = tmp_df[col].astype('str')
            
            match idx:
                case 1:
                    tmp_clr:str = self.CYAN
                case 2:
                    tmp_clr:str = self.ORANGE
                case 3:
                    tmp_clr:str = self.MAGENTA
            
            for r in tmp_df.shape[0]:
                tmp_df.loc[r,col] = f'{tmp_clr}{tmp_df.loc[r,col]}{self.RESET}'

        table:str = tabulate(tabular_data=tmp_df,
                             headers='keys',
                             tablefmt=style
                             )
        return table
    
    def print_legend(self) -> None:
        print('+++ LEGEND +++')

        for cmd,description in self.menu.items():
            print(f' --> {self.BOLD}{cmd}{self.RESET}\t :: {description}')

        return 

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
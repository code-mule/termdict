# bertrandterrier@codeberg.org/termdict/main.py

from ios import first_time,ConfigSettings
from com import get_cl_args
from tabulate import tabulate
import pandas as pd
import sys
import os

# Create the menu legend
MENU:dict = {
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
        """Creates a dictionary object holding the pandas DataFrame, the typographical 
        table string and different information to the dictionary.

        Args:
            csv (str): Path to the CSV file with main dictionary data.
            data_dir (str): Directory to the individual dictionary entries. 
                            Will be "~/.todo/<csv-name>/entries"
            tbl_style (str): Tabulate style name for style of table.
            highlight_cols (dict): Dictionary for highlighted columns.
                                   (1:cyan, 2:orange, 3:magenta)

        Returns:
            int: Return code
        """
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

        for cmd,description in MENU.items():
            print(f' --> {self.BOLD}{cmd}{self.RESET}\t :: {description}')

        return 

def check_return_code(code:str) -> bool:


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

    # Load settings from configuration file
    curr_settings = ConfigSettings()
    
    # Check for data folder
    inp_csv:str = os.path.expanduser(args.input)
    raw_basename,_ = os.path.splitext(os.path.basename(inp_csv))
    inp_dir:str = os.path.dirname(inp_csv)

    entry_dir:str = os.path.join(inp_dir,f'.{raw_basename}_zttl')

    if not os.path.exists(entry_dir):
        entry_dir = f'EMTPY%{entry_dir}'
    

    # Initialize dictionary object
    lexikon = TermDict(csv=args.input,
                       data_dir=entry_dir,
                       tbl_style=curr_settings.get_val("style.table"),
                       highlight_cols=curr_settings.get_val('hl.columns')
                       )
    
    ### MAIN LOOP ###
    fail_counter = 0
    exit_loop = False
    rtn_code = None
    while exit_loop == False:

        # Emergency stop if going on to long
        if abs(fail_counter) >= 1111:
            print(f'== WARNING FAILURE!')
            print('\t::Process looping to long.')
            print('\t== ABORTING...')

            sys.exit(2)

        # Replace possible words
        for h in ['help','HELP','Help']:
            if h in return_code:
                rtn_code = rtn_code.replace(h,'?')
        
        # Split command from arguments
        if ':' in rtn_code:
            command,cmd_args = rtn_code.split(':')
        else:
            command:str = rtn_code
            cmd_args = None

        # Check the command
        force = False
        pre_exit = False
        for c in command:
            match c.lower():
                case 'q':
                    if force == True:
                        sys.exit(3)
                case '?'|'!'|'x':
                    pass
                case ''

    return

if __name__ == "__main__":
    main()
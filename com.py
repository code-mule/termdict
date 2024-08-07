# bertrandterrier@codeberg.org/termdict/com.py

import argparse

def get_cl_args() -> object:
    # Initialize argument parser
    parser = argparse.ArgumentParser(prog="TermDict",
                                     description="A small script for handling a personal dictionary via the command line."
                                     )
    # Add arguments
    parser.add_argument(
        "-i",
        "--input",
        help="Input CSV file."
    )
    parser.add_argument(
        "-f",
        "--find",
        action="store_true",
        help="Replaces input to list CSV files started with the provided directory to choose dictionary from."
    )
    parser.add_argument(
        "-c",
        "--config",
        action="store_true",
        help="Start the configuration settings mode. If chosen all other flags will be ignored."
    )
    parser.add_argument(
        "-n",
        "--new",
        help="Like input, but generated CSV will be set to default dictionary. Please always use for new files and use `--secondary` flag to suppress the default setting."
    )
    parser.add_argument(
        "-sec",
        "--secondary",
        action="store_true",
        help="Use with `--new` flag. Supresses to set new dictionary as default dictionary."
    )
    parser.add_argument(
        "-l",
        "--legend",
        action="store_true",
        help="Show legend without starting main TermDict program."
    )

    # Store arguments
    args = parser.parse_args()

    return args
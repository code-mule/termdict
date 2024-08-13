# Exit Codes

Code    | Location              | Type          | Explanation
-------:|:----------------------|:--------------|:----------------
0       | `main.main`           |               | Ending script without any problems
1       | `main.main`           | __config__    | Exiting program after the configuration settings
2       | `main.main`           | __emergency__ | Looping to long. Emergency stop.
3       | `main.main` _(loop)_  | __forced__    | Force quit by user.
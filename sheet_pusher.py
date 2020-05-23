import gspread
import cmews
from gspread_dataframe import set_with_dataframe

# get dataframe
df = cmews.get_dataframe()

# authenticate
gc = gspread.service_account(filename='<INSERT FILE NAME HERE>.json')

#open file 
sh = gc.open("CME scraper")
ws = sh.worksheet('Copper')

# transfer dataframe to excel
set_with_dataframe(ws, df)
print("Completed upload to Google Sheets")

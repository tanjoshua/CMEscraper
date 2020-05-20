import gspread
import cmews
from gspread_dataframe import set_with_dataframe

# get dataframe
df = cmews.getdataframe()
print(df)

# authenticate
gc = gspread.service_account(filename='cme-scraping-76715bfd0d20.json')

#open file 
sh = gc.open("CME scraper")
ws = sh.worksheet('Copper')

# transfer dataframe to excel
set_with_dataframe(ws, df)
## CME Web Scraper
The Web Scraper is located at cmews.py. The script that uploads the file to google sheets is located at sheet_pusher.py. sheet_pusher.py is the script that you run. geckodriver.exe is essential for the selenium library to work. 

Libraries required can be found in the environment folder. To launch the virtual environment, run .venv/Scripts/activate

## Functionality
Scrapes the web page at https://www.cmegroup.com/trading/metals/base/copper_quotes_volume_voi.html#tradeDate=20200518 and compiles all of the tables into a single pandas dataframe according to Strike price, separated by month. Pushes to a google sheet.

**For privacy reasons**, I have removed the .json authentication key. If you would like to use this script, create a Google service account and place the JSON key in the same directory as this program. Give your service account edit permissions to your google sheet, and change the names of the files in sheet_pusher.py. 

## Bugs
1. Even though the script uses Selenium to wait until the page is fully loaded before scraping the web data, there are instances where the script scrapes the page before the page is fully loaded. Just try it again and it should work.

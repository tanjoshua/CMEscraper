## CME Web Scraper
The Web Scraper is located at cmews.py. The script that uploads the file to google sheets is located at sheetpusher.py. sheetpusher.py is the script that you run. 

Libraries required can be found in the environment folder

If you want sheetpusher.py to push to a different google sheet, give scraper-service-account@cme-scraping.iam.gserviceaccount.com permission to your google sheet 

## Functionality
Scrapes the web page at https://www.cmegroup.com/trading/metals/base/copper_quotes_volume_voi.html#tradeDate=20200518 and compiles all of the tables into a single pandas dataframe according to Strike price, separated by month. Pushes to the google sheet located at https://docs.google.com/spreadsheets/d/1VBLulwDT9GWEQfdEi99isNPxFuDfRGQi75VcJvJE8CE/edit?usp=sharing

## Bugs
1. Even though the script uses Selenium to wait until the page is fully loaded before scraping the web data, there are instances where the script scrapes the page before the page is fully loaded. Just try it again and it should work.
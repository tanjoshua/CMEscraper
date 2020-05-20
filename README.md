## CME Web Scraper
The Web Scraper is located at cmews.py. The script that uploads the file to google sheets is located at sheetpusher.py. sheetpusher.py is the script that you run. 

Libraries required can be found in the environment folder

## Functionality
Scrapes the web page at https://www.cmegroup.com/trading/metals/base/copper_quotes_volume_voi.html#tradeDate=20200518 and compiles all of the tables into a single pandas dataframe according to Strike price, separated by month.

## Bugs
1. In the final dataframe, a row indexed by 75 is not sorted, possibly due to the data being stored as a string. Will have to figure out how to cast that 1 specific index to a float.
2. Even though the script uses Selenium to wait until the page is fully loaded before scraping the web data, there are instances where the script scrapes the page before the page is fully loaded. Just try it again and it should work.
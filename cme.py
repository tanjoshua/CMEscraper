import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

url = 'https://www.cmegroup.com/trading/metals/base/copper_quotes_volume_voi.html#tradeDate=20200518'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers = headers)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
tables = soup.find_all('table')
print(len(tables))



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox()
driver.get('https://www.cmegroup.com/trading/metals/base/copper_quotes_volume_voi.html#tradeDate=20200518')


try:
    element_present = EC.presence_of_element_located((By.ID, 'volumeDetailProductTable'))
    WebDriverWait(driver, 10).until(element_present)
finally:
    print("Page loaded")


dfs = pd.read_html(driver.page_source)

# Split dfs into corresponding data frames
juneCalls = dfs[1]
junePuts = dfs[2]
julCalls = dfs[3]
julPuts = dfs[4]
augCalls = dfs[5]
augPuts = dfs[6]
sepCalls = dfs[7]
sepPuts = dfs[8]
octCalls = dfs[9]
octPuts = dfs[10]
novCalls = dfs[11]
novPuts = dfs[12]
decCalls = dfs[13]
decPuts = dfs[14]
febCalls = dfs[15]
febPuts = dfs[16]


# Create June's dataframe
subcolumns = [['June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Feb'], 
['Strikes', 'Call OI', 'Put OI', 'Total']]
tuples = list(zip(*subcolumns))
print(tuples)
juneResult = pd.DataFrame(columns=['Strikes', 'Call OI', 'Put OI', 'Total'])

rowsList = []
# June calls
for index, row in juneCalls.iterrows():
    strikePrice = row['Strike']['Strike']['Strike']['Strike']['Strike']['Strike']
    oi = row['Open Interest']['At Close']['At Close']['Open Interest']['At Close']['At Close']
    dict1 = {'Strikes': strikePrice, 'Call OI': oi}
    rowsList.append(dict1)
june = pd.DataFrame(rowsList)

# June puts
for index, row in junePuts.iterrows():
    strikePrice = row['Strike']['Strike']['Strike']
    oi = row['Open Interest']['At Close']['At Close']
    june.loc[june['Strikes'] == strikePrice, 'Put OI'] = oi
june['Total'] = june['Call OI'] + june['Put OI']
print(june)
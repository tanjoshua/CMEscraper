from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def getdataframe():
    # launch web browser
    driver = webdriver.Firefox()
    driver.get('https://www.cmegroup.com/trading/metals/base/copper_quotes_volume_voi.html#tradeDate=20200518')

    # Wait for elements to load
    try:
        element_present = EC.presence_of_element_located((By.ID, 'volumesStrikeDataTable'))
        WebDriverWait(driver, 10).until(element_present)
    finally:
        print("Page loaded")

    # use pandas to read all the tables from the web page
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


    # Create dataframe for all months 
    months = ['June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Feb']
    subcolumns = ['Strikes', 'Call OI', 'Put OI', 'Total']
    tuples = [(a,b) for a in months for b in subcolumns]
    index = pd.MultiIndex.from_tuples(tuples)
    df = pd.DataFrame(columns=index)

    # June calls
    for index, row in juneCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('June', 'Call OI')] = oi


    # June puts
    for index, row in junePuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('June', 'Put OI')] = oi

    # July calls
    for index, row in julCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('July', 'Call OI')] = oi

    # July puts
    for index, row in julPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('July', 'Put OI')] = oi    

    # Aug calls
    for index, row in augCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Aug', 'Call OI')] = oi

    # Aug puts
    for index, row in augPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Aug', 'Put OI')] = oi    

    # Sep calls
    for index, row in sepCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Sep', 'Call OI')] = oi

    # Sep puts
    for index, row in sepPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Sep', 'Put OI')] = oi    

    # Oct calls
    for index, row in octCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Oct', 'Call OI')] = oi

    # Oct puts
    for index, row in octPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Oct', 'Put OI')] = oi   

    # Nov calls
    for index, row in novCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Nov', 'Call OI')] = oi

    # Nov puts
    for index, row in novPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Nov', 'Put OI')] = oi  

    # Dec calls
    for index, row in decCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Dec', 'Call OI')] = oi

    # Dec puts
    for index, row in decPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Dec', 'Put OI')] = oi 

    # Feb calls
    for index, row in febCalls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Feb', 'Call OI')] = oi

    # Feb puts
    for index, row in febPuts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Feb', 'Put OI')] = oi   

    # drop 'total' row
    df.drop(['Totals'], inplace = True)
    # Create strike column for each month
    df[('June', 'Strikes')] = df.index
    df[('July', 'Strikes')] = df.index
    df[('Aug', 'Strikes')] = df.index
    df[('Sep', 'Strikes')] = df.index
    df[('Oct', 'Strikes')] = df.index
    df[('Nov', 'Strikes')] = df.index
    df[('Dec', 'Strikes')] = df.index
    df[('Feb', 'Strikes')] = df.index

    # Calculate total for all months
    df.fillna(0, inplace = True)
    df[('June', 'Total')] = df[('June', 'Call OI')] + df[('June', 'Put OI')]
    df[('July', 'Total')] = df[('July', 'Call OI')] + df[('July', 'Put OI')]
    df[('Aug', 'Total')] = df[('Aug', 'Call OI')] + df[('Aug', 'Put OI')]
    df[('Sep', 'Total')] = df[('Sep', 'Call OI')] + df[('Sep', 'Put OI')]
    df[('Oct', 'Total')] = df[('Oct', 'Call OI')] + df[('Oct', 'Put OI')]
    df[('Nov', 'Total')] = df[('Nov', 'Call OI')] + df[('Nov', 'Put OI')]
    df[('Dec', 'Total')] = df[('Dec', 'Call OI')] + df[('Dec', 'Put OI')]
    df[('Feb', 'Total')] = df[('Feb', 'Call OI')] + df[('Feb', 'Put OI')]

    # Sort by descending strike price
    df.sort_index(ascending = False, inplace = True)
    return df
    # print to excel for testing
    # df.to_excel("output.xlsx")

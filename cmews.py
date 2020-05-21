from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def get_dataframe():
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
    june_calls = dfs[1]
    june_puts = dfs[2]
    jul_calls = dfs[3]
    jul_puts = dfs[4]
    aug_calls = dfs[5]
    aug_puts = dfs[6]
    sep_calls = dfs[7]
    sep_puts = dfs[8]
    oct_calls = dfs[9]
    oct_puts = dfs[10]
    nov_calls = dfs[11]
    nov_puts = dfs[12]
    dec_calls = dfs[13]
    dec__puts = dfs[14]
    feb_calls = dfs[15]
    feb_puts = dfs[16]


    # Create dataframe for all months 
    months = ['June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Feb']
    subcolumns = ['Strikes', 'Call OI', 'Put OI', 'Total']
    tuples = [(a,b) for a in months for b in subcolumns]
    index = pd.MultiIndex.from_tuples(tuples)
    df = pd.DataFrame(columns=index)

    # June calls
    for index, row in june_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('June', 'Call OI')] = oi


    # June puts
    for index, row in june_puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('June', 'Put OI')] = oi

    # July calls
    for index, row in jul_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('July', 'Call OI')] = oi

    # July puts
    for index, row in jul_puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('July', 'Put OI')] = oi    

    # Aug calls
    for index, row in aug_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Aug', 'Call OI')] = oi

    # Aug puts
    for index, row in aug_puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Aug', 'Put OI')] = oi    

    # Sep calls
    for index, row in sep_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Sep', 'Call OI')] = oi

    # Sep puts
    for index, row in sep_puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Sep', 'Put OI')] = oi    

    # Oct calls
    for index, row in oct_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Oct', 'Call OI')] = oi

    # Oct puts
    for index, row in oct_puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Oct', 'Put OI')] = oi   

    # Nov calls
    for index, row in nov_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Nov', 'Call OI')] = oi

    # Nov puts
    for index, row in nov_puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Nov', 'Put OI')] = oi  

    # Dec calls
    for index, row in dec_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Dec', 'Call OI')] = oi

    # Dec puts
    for index, row in dec__puts.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Dec', 'Put OI')] = oi 

    # Feb calls
    for index, row in feb_calls.iterrows():
        strikePrice = row['Strike']['Strike']['Strike']
        oi = row['Open Interest']['At Close']['At Close']
        df.loc[strikePrice, ('Feb', 'Call OI')] = oi

    # Feb puts
    for index, row in feb_puts.iterrows():
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

    # convert all indices to ints
    df.index = df.index.map(int)
    # Sort by descending strike price
    df.sort_index(ascending = False, inplace = True)
    return df
    # print to excel for testing
    # df.to_excel("output.xlsx")
import pandas as pd 




singleMonth = pd.MultiIndex.from_product(['month'], ['Strikes', 'Call OI', 'Put OI', 'Total'])
df2 = pd.DataFrame([[1,2,3,4]], columns=singleMonth)
print(df2)
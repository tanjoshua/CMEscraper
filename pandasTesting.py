import pandas as pd 

subcolumns = [['June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Feb'], 
['Strikes', 'Call OI', 'Put OI', 'Total']]
tuples = list(zip(*subcolumns))
print(tuples)
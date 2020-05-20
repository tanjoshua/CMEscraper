import pandas as pd 

months = ['June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Feb']
subcolumns = ['Strikes', 'Call OI', 'Put OI', 'Total']
tuples = [(a,b) for a in months for b in subcolumns]
index = pd.MultiIndex.from_tuples(tuples)
df = pd.DataFrame(columns=index)
df.loc[0, ('June','Call OI')] = 100
df.loc[10, ('June','Call OI')] = 500

df.loc[df[('June','Call OI')] == 100, ('June', 'Strikes')] = 200
print(df)

#check if column exists
print(df[('June', 'Strikes')])
print(200 in df[('June', 'Strikes')].values)

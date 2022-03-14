import pandas as pd


# The function below is downloading a csv file and assigning it to df. However, if you dealing with a very large data
# set you can processes the data in chunk if you want by using the function chucks=x which will upload x rows of the
# data
df = pd.read_csv('pokemon_data.csv')

# the .head(x) or .tail(y) function give you either the top or bottom x columns of data.
# Pandas dataframe is basically a tabular data which has labeled axes (rows and columns)
# Panda dataframes are mutable (can be changed)
# Panda dataframes care composed of three things: the data, rows and colums

print(df.head(3))

# .columns gives the header of the rows for the data
print(df.columns)

# if you want to read the data from just one column you need to use df['header name of column1,header name of column2']

print(df[['Name', 'HP']][0:4])

# To get a row of data you would need to use .iloc

print(df.iloc[0:4])

# to get a specific data you would need to use .iloc[Row number, column number]

print(df.iloc[5, 1])

# for index, row in df.iterrows():
# print(index,row)


# Using the .loc function you can locate data which match a specific requirement. The function below is
# Referred to as a conditional  statements
var = df.loc[df['Type 1'] == "Water"]
print(var)

# The .describe function provide statistical information on your data
poke_stat = df.describe()
print(poke_stat)

# you can use the .sort_values('Name')
poke_stat_sort = df.sort_values(['Type 1', 'HP'], ascending=[1, 0])
print(poke_stat_sort)

print(df.head(5))

# Below we are introducing a new column called Total
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.columns)

# if you want to get rid of a column you would need to use the .drop(columns=['Name of the column']) columns function.

df = df.drop(columns=['Total'])
print(df.columns)

# This adding up all the value from column 4 to 9. The .sum(axis=1) is telling the interpreter to add horizontal not
# vertical.
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

print(df.columns)
print(df.head(5))

cols = list(df.columns.values)
print(cols)

# if you want to save data you would need to use .to_csv('give a name to the file')

df.to_csv('modified.csv', index=False)

# If you want to save the data to an excel file you would need to use the function .to_excel

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
print(new_df)

# Using the .reset_index reet the index column in the data.
new_def = new_df.reset_index(drop=True, inplace=True)
print(new_def)

# If you want to save filtered date which you have made you can do the following below:
new_df.to_csv('filtered_data1')

# .str.contains is a function which telling the python interpreter to find strings which have the word Mega in it
print(df.loc[df['Name'].str.contains('Mega')])

# Alternatly add the ~ at the front of the function tell the python interpreter to avoid all the 'Names' which have
# the word mega in it.

print(df.loc[df['Name'].str.contains('Mega')])

# This line of code is changing the input Fire in the pokeman database into flamer.

df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df)

# The line code below show how to modify each column data individual
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'Test value'

# group by function and carry out statistical analysis on them.

# The line of code below groups the data in terms of 'Type 1' and then  works out the mean for each column. Then the
# .sort_values performer an rearrangement according to Defense

print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

print(df.groupby(['Type 1']).sum().sort_values('HP', ascending=False))

print(df.groupby(['Type 1'].count))

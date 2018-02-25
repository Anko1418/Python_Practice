import pandas as pd

df = pd.read_excel("F:\Python\DataScience\Datasets\DataCleaning-demo_1.xls")

# Print the head of df
#print(df.head())

# Print the tail of df
#print(df.tail())

# Print the shape of df
#print(df.shape)
# it has 189 rows and 5 columns

# Print the columns of df
#print(df.columns)

print(df.info())
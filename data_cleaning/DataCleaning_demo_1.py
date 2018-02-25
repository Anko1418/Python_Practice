import pandas as pd

df = pd.read_excel("F:\Python\DataScience\Datasets\DataCleaning-demo_1.xls")

# Print the head of df
# print(df.head())

# Print the tail of df
# print(df.tail())

# Print the shape of df
# print(df.shape)
# it has 189 rows and 5 columns

# Print the columns of df
# print(df.columns)


# print(df.info())


# Exploratory data analysis

df_columns = df.columns

# print(df[df_columns[0]].value_counts(dropna=False))
# there are 17 NaN

# print(df[df_columns[1]].value_counts(dropna=False))
# there are 12 NaN

# print(df[df_columns[2]].value_counts(dropna=False))
# there are 17 NaN

# print(df[df_columns[3]].value_counts(dropna=False))
# there are 24 NaN

# print(df[df_columns[4]].value_counts(dropna=False))
# there are 25 NaN


# Summary Statistics

print(df.describe())
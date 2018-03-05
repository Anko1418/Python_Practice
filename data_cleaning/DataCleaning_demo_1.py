import pandas as pd
import matplotlib.pyplot as pt

df = pd.read_excel("F:\Python\DataScience\Datasets\DataCleaning-demo_1.xls.xlsx")

# Print the head of df
# print(df.head())

# Print the tail of df
#print(df.tail())

# Print the shape of df
# print(df.shape)
# it has 182 rows and 5 columns

# Print the columns of df
# print(df.columns)


# print(df.info())


# Exploratory data analysis

df_columns = df.columns

#print(df[df_columns[0]].value_counts(dropna=False))
# there are 13 NaN

# print(df[df_columns[1]].value_counts(dropna=False))
# there are 0 NaN

# print(df[df_columns[2]].value_counts(dropna=False))
# there are 13 NaN

# print(df[df_columns[3]].value_counts(dropna=False))
# there are 19 NaN

# print(df[df_columns[4]].value_counts(dropna=False))
# there are 20 NaN


# Summary Statistics

# print(df.describe())

# visualize data
#df['population'].plot('hist')
#pt.interactive(False)
#pt.show()

#print(df[df['population'] > 1000000000])

df.boxplot(column='population', by='Continent')
pt.show()


# import statements
import pandas as pd
import numpy as np

# initialization

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

print(cars)
# prints
#    cars_per_cap        country  drives_right
# 0           809  United States          True
# 1           731      Australia         False
# 2           588          Japan         False
# 3            18          India         False
# 4           200         Russia          True
# 5            70        Morocco          True
# 6            45          Egypt          True

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# assign labels to each row
cars.index = row_labels
print(cars)
# prints
#      cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False
# JAP           588          Japan         False
# IN             18          India         False
# RU            200         Russia          True
# MOR            70        Morocco          True
# EG             45          Egypt          True


# accessing columns from a DataFrame

# print a particular column as Series
print(cars["country"])
# prints
# US     United States
# AUS        Australia
# JAP            Japan
# IN             India
# RU            Russia
# MOR          Morocco
# EG             Egypt
# Name: country, dtype: object

print(type(cars["country"]))
# prints <class 'pandas.core.series.Series'>

# print a particular column as DataFrame
print(cars[["country"]])
# prints
#            country
# US   United States
# AUS      Australia
# JAP          Japan
# IN           India
# RU          Russia
# MOR        Morocco
# EG           Egypt

print(type(cars[["country"]]))
# <class 'pandas.core.frame.DataFrame'>

# for printing more then one column
print(cars[["country", "drives_right"]])
# prints
#            country  drives_right
# US   United States          True
# AUS      Australia         False
# JAP          Japan         False
# IN           India         False
# RU          Russia          True
# MOR        Morocco          True
# EG           Egypt          True


# accessing rows from a DataFrame using loc(label-based)

print(cars.loc[["US", "AUS"]])
# prints 2 rows
#       cars_per_cap        country  drives_right
# US            809  United States          True
# AUS           731      Australia         False

# print rows for particular column
print(cars.loc[["US", "AUS"], ["country"]])
# prints
#            country
# US   United States
# AUS      Australia

# print all rows for given column
print(cars.loc[:, ["country", "drives_right"]])
# prints
#            country  drives_right
# US   United States          True
# AUS      Australia         False
# JAP          Japan         False
# IN           India         False
# RU          Russia          True
# MOR        Morocco          True
# EG           Egypt          True


# accessing rows from a DataFrame using iloc(integer positon based)
# It is same as loc but instead of labels, iloc uses indexs

print(cars.iloc[[1, 2], [2]])
# prints
#      drives_right
# AUS         False
# JAP         False


# operators applied on DataFrame

# show rows where 'drives_right' is equal to 'True' and "cars_per_cap" is greater than 200

print(cars[np.logical_and(cars["drives_right"] == True, cars["cars_per_cap"] > 200)])
# prints
#     cars_per_cap        country  drives_right
# US           809  United States          True


# iterating over DataFrame

for label, row in cars.iterrows():
    print("label: " + label + " row: " + row["country"])
    print('----------------')

# prints
# label: US row: United States
# ----------------
# label: AUS row: Australia
# ----------------
# label: JAP row: Japan


# Manipulating columns in a DataFrame

# add a new column name 'name_length' in cars DataFrame

for label, row in cars.iterrows():
    cars.loc[label, "name_length"] = len(row["country"])

print(cars)

# prints
#      cars_per_cap        country  drives_right   name_length
# US            809  United States          True           13.0
# AUS           731      Australia         False            9.0
# JAP           588          Japan         False            5.0
# IN             18          India         False            5.0
# RU            200         Russia          True            6.0
# MOR            70        Morocco          True            7.0
# EG             45          Egypt          True            5.0

# However above approch is not prefered as each loop ll create a new series object

del(cars["name_length"])

# method mentioned below doesn't take a loop
cars["name_length"] = cars["country"].apply(len)
print(cars)

# another example cars["COUNTRY"] = cars["country"].apply(str.upper)


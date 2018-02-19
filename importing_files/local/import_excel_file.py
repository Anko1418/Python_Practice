# import statements
import pandas as pd

# file path
# more excel files at http://mercury.webster.edu/aleshunas/Data%20Sets/Supplemental%20Excel%20Data%20Sets.htm
file = 'F:\Python\DataScience\Datasets\pnorectic.xls'

# copies the contents of excel file into data variable.
# if you are getting an error for below line, open terminal or cmd and type this 'pip install xlrd'
data = pd.ExcelFile(file)

# prints the names of sheets available in excel file
print(data.sheet_names)
# ['anorectic']

# copy the contents of frist sheet in sheet1 DataFrame
sheet1 = data.parse(data.sheet_names[0])

# print headers
print(sheet1.head())
#      weight  mens  fast  binge  vomit  purge  hyper  fami  eman  frie  ...
# 0         1     1     1      4      4      4      1     1     1     3  ...

# skip second row
data2 = data.parse(0, skiprows=[1])

print(data2)
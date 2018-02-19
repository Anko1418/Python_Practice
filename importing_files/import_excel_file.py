# import statements
import pandas as pd

# file path
file = 'F:\Python\DataScience\Datasets\pnorectic.xls'

# copies the contents of excel file into data variable.
# if you are getting an error for below line, open terminal or cmd and type this 'pip install xlrd'
data = pd.ExcelFile(file)

print(data.sheet_names)

print(data.parse(0))

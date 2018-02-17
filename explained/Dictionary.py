# initialization

python_dict = {"India": 111, "USA": 222, "UK": 333}

multilevel_dict = {'spain': {'capital': 'madrid', 'population': 46.77},
                   'france': {'capital': 'paris', 'population': 66.03},
                   'germany': {'capital': 'berlin', 'population': 80.62},
                   'norway': {'capital': 'oslo', 'population': 5.084}}

# check if a key is present in dictionary
print("india" in python_dict)
# prints True


# Manipulating elements in Dictionary
python_dict["UAE"] = 444
print(python_dict)
# prints {'UK': 333, 'USA': 222, 'UAE': 444, 'India': 111}

del (python_dict["UAE"])
print(python_dict)
# prints {'UK': 333, 'India': 111, 'USA': 222}

# print a particular value of a multilevel dictionary
print(multilevel_dict["spain"]["capital"])
# prints madrid


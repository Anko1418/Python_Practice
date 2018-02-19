# import statements
import pickle

# initialization
demo_data = {"Data1": 0, "Data2": 1, "Data3": 2}

# create a file and copying demo_data contents in the file
pickle.dump(demo_data, open("pickle_example_1.p", "wb"))

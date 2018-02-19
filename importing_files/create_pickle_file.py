import pickle

demo_data = {"Data1": 0, "Data2": 1, "Data3": 2}

pickle.dump(demo_data, open("pickle_example_1.p", "wb"))
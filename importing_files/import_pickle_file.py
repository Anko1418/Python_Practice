# import statements
import pickle as pc

# read and copy the contents of file 'pickle_example_1.p' to variable data
with open('F:\Python\DataScience\Datasets\pickle_example_1.p', 'rb') as file:
    data = pc.load(file)
    print(data)
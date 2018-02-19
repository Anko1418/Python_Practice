import pickle as pc

with open('F:\Python\DataScience\Datasets\pickle_example_1.p', 'rb') as file:
    data = pc.load(file)
    print(data)
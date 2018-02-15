# import statements

import numpy as np

# from numpy import array
# above import statement is not recommended
# If we use it, then we wont be able to different whether the array is from python package or numpy package


# initialization

# list
height = [5.5, 6.5, 7.5, 3.5, 3.5, 9.5, 6.5, 4.5, 7.5, 7.5, 3.5, 7.5, 4.5, 7.5, 9.5]

weight = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69]

# numpy array
np_height = np.array(height)
np_weight = np.array(weight)
np_multivalue_array = np.array([1, 'numpy array can hold multiple data types', True])

# 2D numpy array
np_2d_array = np.array([[1, 2], [3, 4], [5, 6]])

# they are n-dimensional array
print(type(np_multivalue_array))
# prints <class 'numpy.ndarray'>


# proof numpy arrays are single type

print(np.array([1, 'numpy array can hold multiple data types', True]))
# prints and converters all above values to str

print(np.array([1, True]))
# prints [1 1]

print(np.array([1, 1.3]))
# prints [1.  1.3]


# numpy subsettings

# print elements whose height is greater than 6
height_more_than_6 = np_height > 6
print(height_more_than_6)
# prints [False  True  True False False  True  True False  True  True False  True False  True  True]
print(np_height[height_more_than_6])
# prints [6.5 7.5 9.5 6.5 7.5 7.5 7.5 7.5 9.5]

# above code can be written in single line
print(np_height[np_height > 6])


# Dealing with 2D numpy arrays

# print structure of 2D array
print(np_2d_array.shape)
# prints (3, 2) where '3' is the number of rows and '2' is the number of columns

print(np_2d_array[0][0])
# prints 1

print(np_2d_array[0, 1])
# prints 2

print(np_2d_array[:, 0])
# prints [1] [3] [5]

print(np_2d_array[0, :])
# prints [1 2]
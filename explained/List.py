# initialization
python_list = [1, 2, 3, 4, 5, 6]

multivalue_list = ["1", 1, "2", 2, "3", 3]

list_of_lists = [[1, 2], [3, 4], [5, 6]]

# remove list from memory
# del python_list
# if you try to access 'python_list' after above line it ll throw an error saying 'NameError: name 'python_list' is not defined'

# length of list
print(len(python_list))
# prints 6

# Slicing lists

# prints list items 1 to 5.
print(python_list[:-1])

# print list all list items
print(python_list[0:])

# or

print(python_list[:])

# Slicing list of lists

# prints all list items
print(list_of_lists[:])

print(list_of_lists[0])
# prints [1, 2]

print(list_of_lists[0][0])
# prints [1]

print(list_of_lists[-1][-1])
# prints 6


# Changing list elements

python_list[:3] = [0]
print(python_list)
# prints [0, 4, 5, 6]

python_list = [1, 2, 3, 4, 5, 6]
python_list[:3] = [9, 8, 7]
print(python_list)
# prints [9, 8, 7, 6]

python_list = [1, 2, 3, 4, 5, 6]
python_list[:3] = [9, 8, 7, 11, 12]
print(python_list)
# prints [9, 8, 7, 11, 12, 6]

# before
print(multivalue_list)
# prints
multivalue_list[0: 3] = ["change", 11]
# after ["1", 1, "2", 2, "3", 3]
print(multivalue_list)
# prints ['change', 11, 2, '3', 3]


# Adding and removing elements from list
python_list = [1, 2, 3, 4, 5, 6]
multivalue_list = ["1", 1, "2", 2, "3", 3]
list_of_lists = [[1, 2], [3, 4], [5, 6]]

python_list += [7, 8]
print(python_list)
# prints [1, 2, 3, 4, 5, 6, 7, 8]

del [python_list[-1]]
print(python_list)
# prints [1, 2, 3, 4, 5, 6, 7]

del [python_list[-3: -1]]
print(python_list)
# prints [1, 2, 3, 4, 7]

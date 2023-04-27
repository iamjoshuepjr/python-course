# =====================================================================================
#  A set is a collection of unique data. That is, elements of a set cannot be duplicate
#  A set is a collection which is unordered, unchangeable, and unindexed
#  But you can remove items and add new items
# ==================================================================================


# ==================================================================================
#                                  CREATE A SET
#  In python, we create sets by placing all the elements inside culry braces {}, 
#  separated by comma.
#  A set can have any number of items an they may be of different types 
#  (integers, floats, tuples, strings, etc.).
#  But a set cannot have mutable elements like lists, sets or dictionaries as its elements


# ====================================================
#              Empty set
# Creating an empty set is a bit tricky 
# Empty curly braces {} will make an empty dictionary
# To make a set without any elements, we use 
# the set() function without any argument

print('\n\n\t\t\t\t\t+---------------------+')
print('\t\t\t\t\t- CREATE AN EMPTY SET -')
print('\t\t\t\t\t+---------------------+\n')

empty_set = set()
empty_dict = {}

print('\n--------------------------------------------------------')
print(f'* Empty set:   ')
print(f'Set: {empty_set} | Data Type {type(empty_set)}')
print(f'* Empty dict:   ')
print(f'Dict: {empty_dict}  | Data Type {type(empty_dict)}')
print('--------------------------------------------------------')
elements = len(empty_set)
print(f'       Currently the set has: {elements} elements')
elements = len(empty_dict)
print(f'       Currently the dict has: {elements} elements')
print('--------------------------------------------------------\n')

print('\n\n\t\t\t\t\t+--------------+')
print('\t\t\t\t\t- CREATE A SET -')
print('\t\t\t\t\t+--------------+\n')


languages = {'Python', 'Java', 'JavaScript', 'C#', 'C++', 'Python'}
students_id = {100, 101, 102, 103, 104, 105, 106}

print('\n------------------------------------------------------------------------------')
print(f'* Original Students ID List:   ')
print(students_id)
print(f'* Original Languages List:   ')
print(languages)
print('------------------------------------------------------------------------------')
elements = len(students_id)
print(f'       Currently the Studens ID List has: {elements} element(s)')
elements = len(languages)
print(f'       Currently the Languages List has: {elements} element(s)')
print('------------------------------------------------------------------------------\n')
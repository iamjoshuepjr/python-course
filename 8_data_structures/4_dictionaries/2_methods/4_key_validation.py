# =====================================================
#                   Key Validation
#  The all() and any() functions

print('\t\t\t+----------------+')
print('\t\t\t- KEY VALIDATION -')
print('\t\t\t+----------------+\n')

print('1. all() function')
# The .all() function returns True if all elements in the given iterable are true or the iterable is empty.
# If not, it returns False.

# True Iterable
numbers = {1: 'One', 2: 'Two'}
result = all(numbers)

print('\nAll Values True')
print('------------------------')
print('* Number List:   ')
print(numbers)
print('------------------------')
print('Result all() function: ')
print(result)
print('-----------------------')


# One True Value
one_true = {0: 'False', 1: 'True'}
result = all(one_true)

print('\nOne True Value')
print('------------------------')
print('* One True Value List:   ')
print(one_true)
print('------------------------')
print('Result all() function: ')
print(result)
print('-----------------------')

# False Iterable
false_iterable = {0: 'False', 1: False}
result = all(false_iterable)

print('\nAll False Value')
print('------------------------')
print('* Number List:   ')
print(false_iterable)
print('------------------------')
print('Result all() function: ')
print(result)
print('------------------------')

# One False Value
one_false = {0: 'Zero', 1: 'One', 2: False}
result = all(one_false)

print('\nOne False Value')
print('------------------------')
print('* One False Value List:   ')
print(one_false)
print('------------------------')
print('Result all() function: ')
print(result)
print('-----------------------')

# Empty Iterable
users = []
result = all(users)
print('\nEmpty Iterable')
print('------------------------')
print('* Users List:   ')
print(users)
print('------------------------')
print('Result all() function: ')
print(result)
print('------------------------')

print('\n2. any() function')
# The .any() function returns True if all elements of an iterable are true, if one value is True, or one value is false.
# If not (all values are false, an iterable is empty), it returns False.

# True Iterable
languages = {1: 'Python', 2: 'Java'}
result = any(languages)

print('\nAll Values True')
print('------------------------')
print('* Languages List:   ')
print(languages)
print('------------------------')
print('Result any() function: ')
print(result)
print('-----------------------')

# One True Value
one_True = {0: 'False', 1: 'True', 3: False}
result = any(one_True)

print('\nOne True Value')
print('------------------------')
print('* One True Value List:   ')
print(one_True)
print('------------------------')
print('Result any() function: ')
print(result)
print('-----------------------')

# False Iterable
false_Iterable = {0: 'False', False: 0}
result = any(false_Iterable)

print('\nAll False Value')
print('------------------------')
print('* All False Values List:   ')
print(false_Iterable)
print('------------------------')
print('Result any() function: ')
print(result)
print('-----------------------')

# One False Value
one_False = {0: 'Zero', 1: 'One', 2: False}
result = any(one_False)

print('\nOne False Value')
print('------------------------')
print('* One False Value List:   ')
print(one_False)
print('------------------------')
print('Result any() function: ')
print(result)
print('-----------------------')

# Empty Iterable
users = []
result = any(users)
print('\nEmpty Iterable')
print('------------------------')
print('* Users List:   ')
print(users)
print('------------------------')
print('Result any() function: ')
print(result)
print('-----------------------')
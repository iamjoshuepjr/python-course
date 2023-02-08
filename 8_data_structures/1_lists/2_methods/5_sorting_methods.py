# ===============================================================================
#                       Sorting Methods
#  The sort() method sorts the items of a list in ascending or descending order

print()
print('\t\t\t\t   +---------------+')
print('\t\t\t\t   - CREATE A LIST -')
print('\t\t\t\t   +---------------+')
print()

prime_numbers = [11, 3, 7, 5, 2]

print()
print('------------------------------------')
print(f'* Original Prime Numbers List:   ')
print(prime_numbers)
print('--------------------------------------------------------------------------------')
elements = len(prime_numbers)
print(f'             Currently the Prime Numbers List has: {elements} element(s)')
print('--------------------------------------------------------------------------------')
print()
print()

print()
print('\t\t\t    +-------------------------------+')
print('\t\t\t    -      SORTING THE LIST IN      -')
print('\t\t\t    -        ASCENDING ORDER        -')
print('\t\t\t    +-------------------------------+')
print()

print('1 .sort() method')
# By default sort() doesn't require any extra paramaters.
# However, it has two optional parameters:
# reverse - if True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison

prime_numbers.sort()

print('----------------------------------------------')
print(f'  The ascending order is: {prime_numbers}')
print('----------------------------------------------\n')

print('\t\t\t    +-------------------------------+')
print('\t\t\t    -      SORTING THE LIST IN      -')
print('\t\t\t    -        DESCENDING ORDER       -')
print('\t\t\t    +-------------------------------+\n')

prime_numbers.sort(reverse = True)
print('2 .sort(reverse = True) method')
print('----------------------------------------------')
print(f'  The descending order is: {prime_numbers}')
print('----------------------------------------------\n')

numbers = [4, 8, 9, 5, 1, 7, 3, 6, 2, 0]
new_list = sorted(numbers, reverse = True)

print('3 .sorted(list, reverse = True) method')
# The sorted() method doesn't change the list and returns the new sorted list
print('----------------------------------------------------------')
print(f'  The descending order is: {new_list}')
print('----------------------------------------------------------\n')

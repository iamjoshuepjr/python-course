# ========================================================
#                     Values method 
# The values() method returns a view object that displays
# a list of all the values in the dictionary

print('\t\t\t+-----------------+')
print('\t\t\t- VALUES() METHOD -')
print('\t\t\t+-----------------+\n')

print('\t\t\t+---------------------+')
print('\t\t\t- CREATE DICTIONARIES -')
print('\t\t\t+---------------------+\n')

grades = {
    'Physics': 5,
    'Maths': 4
}

sales = {
    'Apple': 5,
    'Orange': 7,
    'Bananas': 4
}

print('1. Dictionary: ')
print('----------------------------------')
print('* Grades Dictionary:   ')
print(grades)
print('----------------------------------\n\n')


print('2. Dictionary: ')
print('----------------------------------')
print('* Sales Dictionary:   ')
print(sales)
print('----------------------------------\n\n')

print('3. Accessig Dictionary Elements (Values): ')
print('------------------')
print(' Sales Dictionary: ')
print('----------------------------------')
print(sales.values())
print('----------------------------------\n\n')

print('4. Removing Dictionary Elements: ')
print('------------------')
print(' Sales Dictionary: ')
print('----------------------------------------------------')
print(sales)
print('----------------------------------------------------')
print('* Delete Apple from Dictionary:   ')
del sales['Apple']
print('\n----------------------')
print(' New Car Dictionary: ')
print('-----------------------------')
print(sales.values())
print('-----------------------------\n')


# ========================================================
#                     Keys method 
# The keys() method extracts the keys of the dictionary 
# and returns the list of keys as a view object

print('\t\t\t+---------------+')
print('\t\t\t- KEYS() METHOD -')
print('\t\t\t+---------------+\n')

# Extracts the keys of the dictionary
print('5. Accessig Dictionary Elements (Keys): ')
print('-------------------')
print(' Grades Dictionary: ')
print('-------------------------------------------------')
print(grades.values())
print('-------------------------------------------------\n\n')
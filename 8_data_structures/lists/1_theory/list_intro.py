# ==================================================================================
#  As developer, you'll frecuently work with sets of data. 
#  You might need to manage multiple names, ages, or addresses.
#  Storing each value in a individual variable makes code harder to read and write.
#  To store multiple values, you can use a Python lists.
# ==================================================================================
#  Python has many built-in types, such as strings and integers
#  Python has a type for storing a collection of values: the list
# ==================================================================================


# ==================================================================================
#                                  CREATE A LIST
#  You create a list by assigning a secuence of values to a variable. Each value is
#  separate by comma and surrounded by brackets []. 
#  For example:

print()
print("\t\t\t\t\t+---------------+")
print("\t\t\t\t\t- CREATE A LIST -")
print("\t\t\t\t\t+---------------+")

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print('\n\n--------------------------------------------------------------------------------------------------')
print(f'* Original Planets List:   ')
print(planets)
print('--------------------------------------------------------------------------------------------------')
elements = len(planets)
print(f'       Currently the Planets List has: {elements} element(s)')
print('--------------------------------------------------------------------------------------------------\n')

# =======================================================================================================
#                                   ACCESSING LIST ITEMS BY INDEX
#  You can access any item in a list by putting the index in brackets [] after the list's variable name
#  Indexes start from 0, so in the following code, planets[0] is the first item in the list planets


print('\n\n\t\t\t\t+-------------------------------+')
print('\t\t\t\t- ACCESSING LIST ITEMS BY INDEX -')
print('\t\t\t\t+-------------------------------+')

print(f'\n* The first planet is: {planets[0]}')
print(f'  planets[0] = {planets[0]}')
print(f'* The second planet is: {planets[1]}')
print(f'  planets[1] = {planets[1]}')
print(f'* The third planet is: {planets[2]}')
print(f'  planets[2] = {planets[2]}')
print(f'* The fourth planet is: {planets[3]}')
print(f'  planets[3] = {planets[3]}')
print(f'* The fifth planet is: {planets[4]}')
print(f'  planets[4] = {planets[4]}')
print(f'* The sixth planet is: {planets[5]}')
print(f'  planets[5] = {planets[5]}')
print(f'* The seventh planet is: {planets[6]}')
print(f'  planets[6] = {planets[6]}')
print(f'* The eighth planet is: {planets[7]}')
print(f'  planets[7] = {planets[7]}')

# ============================================================================
#               ACCESSING LIST ITEMS BY NEGATIVE INDEX
# Negative indexes start at the end of the list and wortk backward
# An index of -1 returns the last item in a list.
# An index of -2 returns the second last item in a list
# So in the following code, planets[-1] is the last item in the list planets

print("\n\n\t\t\t  +----------------------------------------+")
print("\t\t\t  - ACCESSING LIST ITEMS BY NEGATIVE INDEX -")
print("\t\t\t  +----------------------------------------+")

print('\n\t\t\t  Following items are in backward ordered\n')
print(f'* The last planet is: {planets[-1]}')
print(f'  planets[7] = {planets[-1]}')
print(f'* The second last planet is: {planets[-2]}')
print(f'  planets[6] = {planets[-2]}')
print(f'* The third last planet is: {planets[-3]}')
print(f'  planets[5] = {planets[-3]}')
print(f'* The fourth last planet is: {planets[-4]}')
print(f'  planets[4] = {planets[-4]}')
print(f'* The fifth last planet is: {planets[-5]}')
print(f'  planets[3] = {planets[-5]}')
print(f'* The sixth last planet is: {planets[-6]}')
print(f'  planets[2] = {planets[-6]}')
print(f'* The seventh last planet is: {planets[-7]}')
print(f'  planets[1] = {planets[-7]}')
print(f'* The eighth last planet is: {planets[-8]}')
print(f'  planets[0] = {planets[-8]}')
print()

# ==============================================================================
#                ACCESSING LIST ITEMS BY SLICING
# It's posible to acces a section of items from the list the slicing operator

print('\t\t\t  +---------------------------------+')
print('\t\t\t  - ACCESSING LIST ITEMS BY SLICING -')
print('\t\t\t  +---------------------------------+')

print('\n\n------------------------------------------------------------------------------')
print('* Items from index 3 to 6')
print(planets[3:7])
print('\n* Items from 7 to end')
print(planets[7:])
print('\n* Items beginning to end way using slicing')
print(planets[:])
print('------------------------------------------------------------------------------')
elements = len(planets)
print(f'           Currently the Planets List has: {elements} element(s)')
print('------------------------------------------------------------------------------\n')



# =======================================================================================================
#                                CHANGE LIST ITEMS
#  You can also modify values in a list by using an index. You do so by assigning a new value,
#  in much the same way that you would assing a variable value. For example, you could change the name of
#  Mars in the list to use it nickname:

print('\n\t\t\t\t+----------------------+')
print('\t\t\t\t- CHANGING LIST VALUES -')
print('\t\t\t\t+----------------------+')
print()
print(f'* Original Planet List: {planets}')
planets[3] = 'Red Planet'
print(f'* New Planet List: {planets}')
print(f'- Mars was changed to: {planets[3]}')
print()
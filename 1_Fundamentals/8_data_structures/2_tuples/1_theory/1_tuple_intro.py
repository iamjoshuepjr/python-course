# =======================================================================
#  A tuple in Python is similar to a list. The difference between the two 
#  is that we cannot change the elements of a tuple once it is assigned 
#  whereas we can change the element of a list

# ===================================================================================
#                                 CREATE A TUPLE
#  You create a tuple by assigning a secuence of values to a variable. Each value is
#  separate by comma and surrounded by parentheses (). 
#  For example:

print('\n\n\t\t\t\t\t+----------------+')
print('\t\t\t\t\t- CREATE A TUPLE -')
print('\t\t\t\t\t+----------------+\n')


empty_tuple = ()
print('1. Empty tuple: ')
print('-----------------------')
print('* Empty Tuple:   ')
print(empty_tuple)
print('-----------------------')
elements = len(empty_tuple)
print(f'                             Currently the Empty Tuple has: {elements} elements')
print('                           -------------------------------------------------\n')

print('2. Tuple with the same type of elements: ')

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
week = ('Sunday', 'Monday', 'Tuesday', 'Wendnesday', 'Thursday', 'Friday', 'Saturday')

print('---------------------------------------------------------------------------------------------------------------------------')
print('* Tuple having strings:   ')
print(months)
print(week)
print('---------------------------------------------------------------------------------------------------------------------------')
elements_month = len(months)
elements_week = len(week)
print(f'                             Currently the Months Tuple has: {elements_month} elements')
print(f'                             Currently the Week Tuple has: {elements_week} elements')
print('                           -------------------------------------------------\n')

print('3. Tuple with mixed elements: ')

mixed = ('Mercedez Benz', 24, 99.01)

print('------------------------------')
print('* Mixed Tuple: ')
print(mixed)
print('------------------------------')
elements = len(mixed)
print(f'                             Currently the Mixed Tuple has: {elements} elements')
print('                           -------------------------------------------------\n')

print('4. Nested tuple')

nested = ('Bucaramanga', [45, 67, 89], (1, 2, 3))

print('-----------------------------------------')
print('* Nested Tuple: ')
print(nested)
print('-----------------------------------------')
elements = len(nested)
print(f'                             Currently the Empty Tuple has: {elements} elements')
print('                           -------------------------------------------------\n')

# =======================================================================================================
#                                   ACCESSING TUPLES ITEMS BY INDEX
#  You can access any item in a tuple by putting the index in brackets [] after the tuple's variable name
#  Indexes start from 0, so in the following code, months[0] is the first item in the months tuple


print('\n\n\t\t\t\t+--------------------------------+')
print('\t\t\t\t- ACCESSING TUPLE ITEMS BY INDEX -')
print('\t\t\t\t+--------------------------------+')

print(f'\n* The first month is: {months[0]}')
print(f'  months[0] = {months[0]}')
print(f'\n* The second month is: {months[1]}')
print(f'  months[1] = {months[1]}')
print(f'\n* The third month is: {months[2]}')
print(f'  months[2] = {months[2]}')
print(f'\n* The fourth month is: {months[3]}')
print(f'  months[3] = {months[3]}')
print(f'\n* The fifth month is: {months[4]}')
print(f'  months[4] = {months[4]}')
print(f'\n* The sixth month is: {months[5]}')
print(f'  months[5] = {months[5]}')
print(f'\n* The seventh month is: {months[6]}')
print(f'  months[6] = {months[6]}')
print(f'\n* The eighth month is: {months[7]}')
print(f'  months[7] = {months[7]}')
print(f'\n* The nineth month is: {months[8]}')
print(f'  months[8] = {months[8]}')
print(f'\n* The tenth month is: {months[9]}')
print(f'  months[9] = {months[9]}')
print(f'\n* The eleventh month is: {months[10]}')
print(f'  months[10] = {months[10]}')
print(f'\n* The twelfth month is: {months[11]}')
print(f'  months[11] = {months[11]}')

# ===========================================================================
#                 ACCESSING LIST ITEMS BY NEGATIVE INDEX
#  Negative indexes start at the end of the tuple and work backward
#  An index of -1 returns the last item in a tuple
#  An index of -2 returns the second last item in a tuple
#  So in the following code, months[-1] is the last item in the months list

print("\n\n\t\t\t  +----------------------------------------+")
print("\t\t\t  - ACCESSING LIST ITEMS BY NEGATIVE INDEX -")
print("\t\t\t  +----------------------------------------+")

print('\n\t\t\t  Following items are in backward ordered\n')
print(f'\n* The last month is: {months[-1]}')
print(f'  months[11] = {months[-1]}')
print(f'\n* The second last month is: {months[-2]}')
print(f'  months[10] = {months[-2]}')
print(f'\n* The third last month is: {months[-3]}')
print(f'  months[9] = {months[-3]}')
print(f'\n* The fourth last month is: {months[-4]}')
print(f'  months[8] = {months[-4]}')
print(f'\n* The fifth last month is: {months[-5]}')
print(f'  months[7] = {months[-5]}')
print(f'\n* The sixth last month is: {months[-6]}')
print(f'  months[6] = {months[-6]}')
print(f'\n* The seventh last planet is: {months[-7]}')
print(f'  months[5] = {months[-7]}')
print(f'\n* The eighth last month is: {months[-8]}')
print(f'  months[4] = {months[-8]}')
print(f'\n* The nineth last month is: {months[-9]}')
print(f'  months[3] = {months[-9]}')
print(f'\n* The tenth last month is: {months[-10]}')
print(f'  months[2] = {months[-10]}')
print(f'\n* The eleventh last month is: {months[-11]}')
print(f'  planets[1] = {months[-11]}')
print(f'\n* The twelfth last month is: {months[-12]}')
print(f'  months[0] = {months[-12]}')

# ==============================================================================
#                ACCESSING TUPLES ITEMS BY SLICING
# It's posible to acces a section of items from the list the slicing operator

print('\t\t\t  +-----------------------------------+')
print('\t\t\t  - ACCESSING TUPLES ITEMS BY SLICING -')
print('\t\t\t  +-----------------------------------+')

print('\n\n------------------------------------------------------------------------------')
print('* Items from index 3 to 6')
print(months[3:7])
print('\n* Items from 7 to end')
print(months[7:])
print('\n* Items beginning to end way using slicing')
print(months[:])
print('--------------------------------------------------------------------------------------------------------------------------')
elements = len(months)
print(f'                       Currently the Planets List has: {elements} elements')
print('                   ---------------------------------------------------\n')

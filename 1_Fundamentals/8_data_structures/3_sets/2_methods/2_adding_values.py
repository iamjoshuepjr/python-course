# =================================================================================
#                                ADD VALUES TO SET
#  Set in Python are dynamic: you can add and remove items after they're created.
#  However, since they are unordered, indexind has no meaning.
#  We cannot access or change an element of a set using indexing or slicing.
#  Set data type does not support it

print('\n\n\t\t\t\t\t+--------------+')
print('\t\t\t\t\t- CREATE A SET -')
print('\t\t\t\t\t+--------------+\n')

fruits = {'Orange', 'Apple', 'Banana', 'Mango', 'Avocado', 'Pineapple'}

print('------------------------------------------------------------------------------')
print(f'* Original Fruits Set:   ')
print(fruits)
print('------------------------------------------------------------------------------')
elements = len(fruits)
print(f'                 Currently the Fruits Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')

print('\t\t\t     +--------------------------+')
print('\t\t\t     - ADDING NEW VALUES TO SET -')
print('\t\t\t     -         METHODS          -')
print('\t\t\t     +--------------------------+\n\n')
print('--------------------')
print('1. add() method ')
# Add an item to a set
to_add = 'Coconut'
fruits.add(to_add)

print('----------------------------------------------------------------------------')
print(f'* New Fruits Set:   ')
print(fruits)
print(f'* The elemetn {to_add} was added')
print('------------------------------------------------------------------------------')
elements = len(fruits)
print(f'                 Currently the Fruits Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')

print('--------------------')
print('2 .update() method ')
# The update add items from set A to set B (or more sets) 
# and update the set A with the resulting set
# The update method can take any number of arguments

tropical_fruits = {'Dragon Fruit', 'Passion Fruit', 'Acai'}
exotics_fruits = {'Tomate de Árbol', 'Lulo', 'Guayaba'}
fruits.update(tropical_fruits, exotics_fruits)

print('---------------------------------------------------------------------------------------------------------------------')
print(f'* New Fruits Set:   ')
print(fruits)
print(f'Set tropical fruits {tropical_fruits} was added')
print(f'Set exotics fruits {exotics_fruits} was added')
print('---------------------------------------------------------------------------------------------------------------------')
elements = len(fruits)
print(f'                 Currently the Fruits Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')

print('--------------------')
print('3 .copy() method ')
# the copy() method returns a copy of the set; the method doesn't take any parameters
fruits_copy = fruits.copy()

print('---------------------------------------------------------------------------------------------------------------------')
print(f'* New Fruits Set: (Copy from fruits + tropical fruits) ')
print(fruits)
print('---------------------------------------------------------------------------------------------------------------------')
elements = len(fruits)
print(f'                 Currently the Fruits Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')

print('-------------------------------')
print('4 Copy Set by using = Operator ')
print('-------------------------------')
# we can also copy the set by simply using the = operator

print('\n\t\t\t\t\t+--------------+')
print('\t\t\t\t\t- CREATE A SET -')
print('\t\t\t\t\t+--------------+\n')

singers = {'Criss Brown', 'Post Malone', 'The Weeknd'}
print('------------------------------------------------------------------------------')
print(f'* Original Singers Set:   ')
print(singers)
print('------------------------------------------------------------------------------')
elements = len(singers)
print(f'                 Currently the singers Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')
# copy set using = operator
new_singers = singers 
print('------------------------------------------------------------------------------')
print(f'* New Singers Set: (Copy using = operator) ')
print(new_singers)
print('------------------------------------------------------------------------------')
elements = len(new_singers)
print(f'               Currently the New Singers Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')

print('------------------------------------')
print('4.1 Add items to the Set after copy ')
print('------------------------------------\n')

new_singers.add('Drake')
print('------------------------------------------------------------------------------')
print(f'* New Singers Set: (Adding after copy) ')
print(new_singers)
print('------------------------------------------------------------------------------')
elements = len(new_singers)
print(f'               Currently the New Singers Set has: {elements} element(s)')
print('            ----------------------------------------------------\n\n')


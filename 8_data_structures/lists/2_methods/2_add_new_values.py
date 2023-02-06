# =================================================================================
#                                ADD VALUES TO LIST
#  List in Python are dynamic: you can add and remove items after they're created.

print('\n\n\t\t\t\t   +---------------+')
print('\t\t\t\t   - CREATE A LIST -')
print('\t\t\t\t   +---------------+\n\n')

currencies = ['Dollar', 'Euro', 'British Pound']
print(f'* Currencies List: {currencies}')
element = len(currencies)
print(f'* Currencies List has: {element} element(s)\n\n')

print('\t\t\t     +---------------------------+')
print('\t\t\t     - ADDING NEW VALUES TO LIST -')
print('\t\t\t     -           METHODS         -')
print('\t\t\t     +---------------------------+\n\n')

print('1 .append() method')
# The append() method adds an item to the end of the list
# Syntyax: list.append(element)

print()
print('------------------------------------------------------------------')
print(f'* Original Currencies List: {currencies}  *')
currencies.append('Yen')
print('------------------------------------------------------------------')
print('*')
print(f'* New Currencies List: {currencies}')
print(f'* A new value was added: [{currencies[-1]}]')
elements = len(currencies)
print('------------------------------------------------------------------')
print(f'      Currently the Currencies List has: {elements} element(s)')
print('------------------------------------------------------------------')
print()
print()

print('2 .insert() method')
# The .insert() method inserts an element to the list at the specified index
# The .insert() method takes two parameters: 
# - index (where the element needs to be inserted) 
# - element (the element to be inserted in the list)
#           Syntyax: list.insert(i, element)

print()
print('--------------------------------------------------------------------------------')
print(f'* New Original Currencies List: {currencies}     *')
print('--------------------------------------------------------------------------------')
insert = 'Canadian Dollar'
print(f'* New element to add to Currencies List at index 2: [{insert}]')
currencies.insert(2, insert)
elements = len(currencies)

print(f'* New Planet List: {currencies}')
print(f'* A new value was added: [{currencies[2]}]')
print('--------------------------------------------------------------------------------')
print(f'            Currently the Currencies List has: {elements} element(s)')
print('--------------------------------------------------------------------------------')
print()
print()

print('\t\t\t\t   +----------------------+')
print('\t\t\t\t   - CREATE TWO NEW LISTS -')
print('\t\t\t\t   +----------------------+\n\n')

print('3 .extend() method\n\n')
# The .extend() method adds all the elements of an iterable (list, tuple, string...) 
# to the end of the list

back_end = ['Python', 'DDBB', 'C#', 'Java', 'Nodejs']
front_end = ['Html & Css', 'JavaScript', 'React']

print('-----------------------------------------------------------------')
print(f'* Back End List: {back_end}     *')
print('-----------------------------------------------------------------')
print(f'* Front End List: {front_end}         *')
print('-----------------------------------------------------------------')
print()

front_end.extend(back_end)
elements = len(front_end)
print()
print('--------------------------------------------------------------------------------------------------------')
print(f'* Back End List: {back_end} was added to Front End List')
print(f'* New Front End List: {front_end}')
print('--------------------------------------------------------------------------------------------------------')
print(f'                     Currently the Front End List has: {elements} element(s)')
print('--------------------------------------------------------------------------------------------------------\n\n')


print('\t\t\t\t   +----------------------+')
print('\t\t\t\t   - CREATE TWO NEW LISTS -')
print('\t\t\t\t   +----------------------+\n\n')

g7 = ['United States', 'United Kingdom', 'Canada', 'France', 'Germany', 'Italy', 'Japan']

print('4. copy() method\n')
# The copy() method returns a shallow copy of the list
group_seven = g7.copy()
elements_g7 = len(g7)
elements = len(group_seven)

print('-------------------------------------------------------------------------------------------------------------------------------------')
print(f'* G7 List: {g7} was added to Group Seven List')
print(f'* Group Seven List: {group_seven}')
print('-------------------------------------------------------------------------------------------------------------------------------------')
print(f'        Currently the G7 List has: {elements} element(s)')
print(f'        Currently the Group Seven List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')

print('----------------------------------------------------------------')
print(f' If we modify the new list, the old list will not be modified  ')     
print('----------------------------------------------------------------\n\n')

to_add = 'Wales'
print(f'* Adding {to_add} to the new list Group Seven: ')
group_seven.append(to_add)
elements = len(group_seven)

print('-------------------------------------------------------------------------------------------------------------------------------------')
print(f'* G7 List: {g7}')
print(f'* Group Seven Modified List: {group_seven}')
print('-------------------------------------------------------------------------------------------------------------------------------------')
print(f'        Currently the Group Seven List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------------\n\n')

print('5. copy a list with assign ( = ) operator method\n')

winter = ['Dicember', 'January', 'February', 'March']
swon_down = winter

elements = len(winter)
elements_new_list = len(swon_down)
       
print('---------------------------------------------------------------------------------------------')
print(f'* Winter List: {winter} was added to Snow Down List')
print(f'* Snow Down List: {swon_down}')
print('---------------------------------------------------------------------------------------------')
print(f'   Currently the Winter List has: {elements} element(s)')
print(f'   Currently the Snow Down List has: {elements_new_list} element(s)')
print('---------------------------------------------------------------------------------------------\n\n')

print('-------------------------------------------------------------')
print(f' If we modify the new list, the old list is also modified   ')     
print(f' because the new list is referencing the same object (list) ')     
print('-------------------------------------------------------------\n\n')

to_add = 'May'
print(f'* Adding {to_add} to the Snow Down List')
swon_down.append(to_add)

print('---------------------------------------------------------------------------------------------')
print(f'* Winter List: {winter} was added to Snow Down List')
print(f'* Snow Down List: {swon_down}')
print('---------------------------------------------------------------------------------------------')
print(f'   Currently the Winter List has: {elements} element(s)')
print(f'   Currently the Snow Down List has: {elements_new_list} element(s)')
print('---------------------------------------------------------------------------------------------\n\n')

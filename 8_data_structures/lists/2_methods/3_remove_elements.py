# =================================================================================
#                             REMOVE VALUES FROM LIST
#  List in Python are dynamic: you can add and remove items after they're created.
#  To remove the last item in a list, use the .pop() method 


print()
print("\t\t\t\t   +---------------+")
print("\t\t\t\t   - CREATE A LIST -")
print("\t\t\t\t   +---------------+")
print()

teams = ['Arsenal', 'Man City', 'Man United', 'Newcastle', 'Tottenham', 'Liverpool', 'Chelsea', 'Aston Villa', 'Cristal Palace']
print()
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football List:   ')
print(teams)
elements = len(teams)
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------')
print()
print()

print()
print("\t\t\t    +-----------------------------+")
print("\t\t\t    - REMOVING NEW VALUES TO LIST -")
print("\t\t\t    -           METHODS           -")
print("\t\t\t    +-----------------------------+")
print()

print('-------------------------------------------------------------------------------------------------------------------------------')
print('1 .pop() method | without passed argument')
# The pop() method removes the item at the given index from the list an returns the removed item
# Syntyax: list.pop(index)
# The argument passed is optional. If not passed, the default index -1 (index of the last item) is passed as an argument
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football List:   ')
print(teams)
lastElement = teams[-1]
print('-------------------------------------------------------------------------------------------------------------------------------')
print('*')
print(f'* The last element [{lastElement}] is going to be deleted')
# without passed argument
teams.pop()
print(f'* New Football List: {teams}')
elements = len(teams)
print(f'* The last element [{lastElement}] was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------')
print()
print()
print('-------------------------------------------------------------------------------------------------------------------------------')
print('2 .pop() method | with passed argument')
# with passed argument
to_delete = teams[4]
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* The element [{to_delete}] is going to be deleted')
# with passed argument
teams.pop(4)
print(f'* New Football List: {teams}')
elements = len(teams)
print(f'* The element [{to_delete}] was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------')
print()
print()

print('-------------------------------------------------------------------------------------------------------------------------------')
print('3 .remove() method ')
# The .remove() method removes the first matching element from the list
# The .remove() method takes a single element as an argument and removes it from the list
# if the element does not exist, it throws ValueError:list.remove(x): x not in list exception

# with passed argument
to_remove = teams[4]
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* The element [{to_remove}] is going to be deleted')
# with passed argument
teams.remove(to_remove)
print(f'* New Football List: {teams}')
elements = len(teams)
print(f'* The element [{to_remove}] was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------')
print()
print()

print('-------------------------------------------------------------------------------------------------------------------------------')
print('4 .clear() method ')
# The clear() method removes all items from the list
# Syntyax: list.clear()
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football List:   ')
print(teams)
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* All the elements are going to be deleted')
teams.clear()
print(f'* New Football List: {teams}')
elements = len(teams)
print(f'* The whole list was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football List has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------')
print()
print()

print()
print("\t\t\t\t   +---------------+")
print("\t\t\t\t   - CREATE A LIST -")
print("\t\t\t\t   +---------------+")
print()
tech_companies = ['Apple', 'Netflix', 'Microsoft', 'Google', 'Amazon', 'Apple', 'Meta', 'Tesla', 'NVIDIA', 'Amazon', 'Meta', 'Samsung', 'Alibaba', 'Oracle', 'Netflix', 'Intel']

print()
print('------------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Tech Companies List:   ')
print(tech_companies)
print('------------------------------------------------------------------------------------------------------------------------------------')
elements = len(tech_companies)
print(f'               Currently the Tech Companies List has: {elements} element(s)')
print('------------------------------------------------------------------------------------------------------------------------------------')
print()


print("\t\t\t    +-------------------------------+")
print("\t\t\t    - REMOVING VALUES FROM THE LIST -")
print("\t\t\t    -           METHODS             -")
print("\t\t\t    +-------------------------------+")
print()

print('------------------------------------------------------------------------------------------------------------------------------------')
print('5. del operator | Deleting a specific element passed by index ')
# The Python del keyword is used to delete objects
# Syntyax: del object_name

print('------------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Tech Companies List:   ')
print(tech_companies)
to_delete = tech_companies[5]
print('------------------------------------------------------------------------------------------------------------------------------------')
print('*')
print(f'* The element [{to_delete}] is going to be deleted')
del tech_companies[5]
print(f'* New Tech Companies List: {tech_companies}')
elements = len(tech_companies)
print(f'* The last element [{to_delete}] was deleted')
print('------------------------------------------------------------------------------------')
print(f'          Currently the Tech Companies List has: {elements} element(s)')
print('------------------------------------------------------------------------------------')
print()
print('----------------------------------------------------------')
print('5. del operator | Deleting the whole list ')
print('----------------------------------------------------------')
print(f'* All the elements are going to be deleted')
del tech_companies[:]
print(f'* New Tech Companies List: {tech_companies}')
elements = len(tech_companies) 
print(f'* The whole list was deleted')
print('----------------------------------------------------------')
print()
# =================================================================================
#                             REMOVE VALUES FROM SETS
#  Set in Python are dynamic: you can add and remove items after they're created.
#  To remove an specified item from a set, use the .discard() method 

print('\n\t\t\t\t   +---------------+')
print('\t\t\t\t   - CREATE A SET -')
print('\t\t\t\t   +---------------+\n\n')

teams = {'Arsenal', 'Man City', 'Man United', 'Newcastle', 'Tottenham', 'Liverpool', 'Chelsea', 'Aston Villa', 'Cristal Palace'}

print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football Set:   ')
print(teams)
elements = len(teams)
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football Set has: {elements} element(s)')
print('-------------------------------------------------------------------------------------------------------------------------------\n\n')

print('\t\t\t    +---------------------------+')
print('\t\t\t    - REMOVING VALUES FROM SET  -')
print('\t\t\t    -          METHODS          -')
print('\t\t\t    +---------------------------+\n\n')

print('-----------------------')
print('1 .descard() method ')
# The dicard() method removes the specified item from a set 

print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football Set:   ')
print(teams)
print('-------------------------------------------------------------------------------------------------------------------------------')
element = 'Arsenal'
teams.discard(element)

print('\n-------------------------------------------------------------------------------------------------------------------------------')
print(f'* New Football Set:')
print(teams)
print('* The element {'+element+'} was deleted')
elements = len(teams)
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football Set has: {elements} element(s)')
print('                             --------------------------------------------------------\n')

print('-------------------------------------------')
print('2 .pop() method | without passed argument')
# The pop() method removes the item at the given index from the set an returns the removed item
# Syntyax: set.pop()

print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football set:   ')
print(teams)
removed = teams.pop()
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* New Football set: {teams}')
elements = len(teams)
print('* The element {'+removed+'} is was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football Set has: {elements} element(s)')
print('                             --------------------------------------------------------\n')

print('---------------------')
print('3 .remove() method')
# The remove() method removes the specified element from the set
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football set:   ')
print(teams)
to_remove = 'Liverpool'
print('*')
print('* The element {'+to_remove+'} is going to be deleted')
teams.remove(to_remove)
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* New Football set: {teams}')
elements = len(teams)
print('* The element {'+to_remove+'} was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football Set has: {elements} element(s)')
print('                             --------------------------------------------------------\n')

print('--------------------')
print('4 .clear() method')
# The clear() method removes all items from the set
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* Original Football set:   ')
print(teams)
teams.clear()
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* New Football set: {teams}')
elements = len(teams)
print('* The whole set was deleted')
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'                                 Currently the Football Set has: {elements} element(s)')
print('                             --------------------------------------------------------\n')
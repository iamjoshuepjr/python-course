# =============================================================
#                    Set Operators       
# Python Set Provides differents built-in methods to perfrom
# mathematical set operations like 
# union, intersection, substraction, and symmetric difference

print('\n\n\t\t\t\t\t+--------------+')
print('\t\t\t\t\t- CREATE A SET -')
print('\t\t\t\t\t+--------------+\n')

back_end = {'Python', 'DDBB', 'C#', 'Java', 'Nodejs'}
front_end = {'Html & Css', 'JavaScript', 'React'}

print('\n\t\t\t\t+-----------------+')
print('\t\t\t\t- SETS OPERATIONS -')
print('\t\t\t\t+-----------------+\n')

print('---------------------')
print('1. Union of Two Sets')
print('---------------------\n')
# Include all the elements of set A and B

print('-----------------------------------------------------')
print(f'* Original Back-End Set:   ')
print(back_end)
print(f'* Original Front-End Set:   ')
print(front_end)
print('-----------------------------------------------------')
elements = len(back_end)
print(f'   Currently the Back-End Set has: {elements} elements')
elements = len(front_end)
print(f'   Currently the Front-End Set has: {elements} elements')
print('-----------------------------------------------------\n')

print('---------------------------------------')
print(f'1.1 Performin union operation using |')
full_stack = back_end | front_end
print('-------------------------------------------------------------------------------------------------------------------------------')
print(f'* New Full-Stack set: {full_stack}')
elements = len(full_stack)
print('----------------------------------------------------------------------------------------------------------------')
print(f'                               Currently the Full-Stack Set has: {elements} elements')
print('                             ---------------------------------------------------\n')

frameworks_back_end = {'Django', 'Laravel', 'Flask', 'ASP.NET', 'Express.js'}
frameworks_front_end = {'React', 'Angular', 'Vue.js', 'jQuery', 'Backbone.js'}

print('-----------------------------------------------------')
print(f'* Original Frameworks Back-End Set:   ')
print(frameworks_back_end)
print(f'* Original Frameworks Front-End Set:   ')
print(frameworks_front_end)
print('-----------------------------------------------------')
elements = len(frameworks_back_end)
print(f'   Currently the Back-End Set has: {elements} elements')
elements = len(frameworks_front_end)
print(f'   Currently the Front-End Set has: {elements} elements')
print('-----------------------------------------------------\n')

print('-----------------------------------------------------')
print(f'1.2 Performin union operation using .union() method ')
frameworks_full_stack = frameworks_back_end.union(frameworks_front_end)
print('----------------------------------------------------------------------------------------------------------------')
print(f'* New Frameworks Full-Stack set:')
print(frameworks_full_stack)
elements = len(frameworks_full_stack)
print('----------------------------------------------------------------------------------------------------------------')
print(f'                               Currently the Frameworks Full-Stack set has: {elements} elements')
print('                             -------------------------------------------------------------\n')

print('--------------------')
print('2. Set Intersection ')
print('--------------------\n')
# The intersection of two sets A and B include the common elements between set A and B

setA = {1, 4, 7, 10, 13}
setB = {1, 5, 10, 13, 4}

print('-------------------------------------')
print(f'* Original Set A:  {setA} ')
print(f'* Original Set B:  {setB} ')
print('-------------------------------------')
elements = len(setA)
print(f' Currently the Set A has: {elements} elements')
elements = len(setB)
print(f' Currently the Set B has: {elements} elements')
print('-------------------------------------\n')


print('----------------------------------------------')
print(f'2.1 Performin intersection operation using &')
intersection = setA & setB
print('-------------------------------------')
print(f'* Intersection set: {intersection}')
elements = len(intersection)
print('-------------------------------------')
print(f'                   Currently the Intersection Set has: {elements} elements')
print('                  ---------------------------------------------------\n')


setC = {2, 5, 8, 11, 14}
setD = {2, 6, 11, 14, 5}

print('-------------------------------------')
print(f'* Original Set C:  {setC} ')
print(f'* Original Set D:  {setD} ')
print('-------------------------------------')
elements = len(setC)
print(f' Currently the Set C has: {elements} elements')
elements = len(setD)
print(f' Currently the Set D has: {elements} elements')
print('-------------------------------------\n')

print('-----------------------------------------------------------')
print(f'2.2 Performin intersection operation using .intersection()')
intersection = setC.intersection(setD)
print('-----------------------------------------------------------------------------------------')
print(f'* Intersection set: {intersection}')
elements = len(intersection)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Intersection Set has: {elements} elements')
print('                  ---------------------------------------------------\n')

print('--------------------')
print('3. Set Diference ')
print('--------------------\n')
# The difference between two sets A and B include the common elements of the set A that aren not present on set B

setE = {2, 6, 7, 11, 14}
setF = {2, 63, 16, 14, 5}

print('-------------------------------------')
print(f'* Original Set E:  {setE} ')
print(f'* Original Set F:  {setF} ')
print('-------------------------------------')
elements = len(setE)
print(f' Currently the Set E has: {elements} elements')
elements = len(setF)
print(f' Currently the Set F has: {elements} elements')
print('-------------------------------------\n')

print('-----------------------------------------------------')
print(f'3.1 Performin difference operation using - operator')
difference = setE - setF
print('-----------------------------------------------------')
print(f'* Difference set E - F: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Difference E - F Set has: {elements} elements')
print('                  ---------------------------------------------------\n')
difference = setF - setE
print(f'* Difference set F - E: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Difference F - E Set has: {elements} elements')
print('                  ---------------------------------------------------\n')


setG = {4, 8, 14, 21, 28}
setH = {4, 63, 16, 14, 5}

print('-------------------------------------')
print(f'* Original Set G:  {setG} ')
print(f'* Original Set H:  {setH} ')
print('-------------------------------------')
elements = len(setG)
print(f' Currently the Set G has: {elements} elements')
elements = len(setH)
print(f' Currently the Set H has: {elements} elements')
print('-------------------------------------\n')

print('-------------------------------------------------------')
print(f'3.2 Performin difference operation using .difference')
difference = setG.difference(setH)
print('-----------------------------------------------------')
print(f'* Difference set G - H: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Difference Set G - H has: {elements} elements')
print('                  ---------------------------------------------------\n')

difference = setH.difference(setG)
print(f'* Difference set H - G: {difference}')
elements = len(difference)
print(f'                   Currently the Difference Set H - G has: {elements} elements')
print('                  ---------------------------------------------------\n')

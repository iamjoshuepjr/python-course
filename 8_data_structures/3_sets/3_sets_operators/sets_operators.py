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
print(f'1.1 performing union operation using |')
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
print(f'1.2 performing union operation using .union() method ')
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


print('-----------------------------------------------')
print(f'2.1 performing intersection operation using &')
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
print(f'2.2 performing intersection operation using .intersection()')
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
print(f'3.1 performing difference operation using - operator')
difference = setE - setF
print('-----------------------------------------------------')
print(f'* Difference set E - F: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Difference E - F Set has: {elements} elements')
print('                  ---------------------------------------------------\n')

print('----------------------------------------------------------------')
print(f'3.2 performing difference operation using .difference() method')
difference = setF.difference(setE)
print('-----------------------------------------------------')
print(f'* Difference set E - F: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Difference Set E - F has: {elements} elements')
print('                  ---------------------------------------------------\n')

print('--------------------------')
print('4. Set Symetric Diference ')
print('--------------------------\n')
# The symmetric difference between two sets A and B include all elements of A and B without the common elements
# We use the ^ operator, and/or symetric_difference() method to perform symmetric difference between two sets

setG = {24, 56, 67, 89}
setH = {56, 89, 79, 59}

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
print(f'4.1 performing difference operation using ^ operator ')
difference = setG ^ setH
print('-----------------------------------------------------')
print(f'* Difference set G - H: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Symetric Difference Set G - H has: {elements} elements')
print('                  ---------------------------------------------------------------\n')

setI = {28, 24, 90, 18}
setJ = {24, 18, 79, 59}

print('-------------------------------------')
print(f'* Original Set I:  {setI} ')
print(f'* Original Set J:  {setJ} ')
print('-------------------------------------')
elements = len(setI)
print(f' Currently the Set I has: {elements} elements')
elements = len(setJ)
print(f' Currently the Set J has: {elements} elements')
print('-------------------------------------\n')

print('--------------------------------------------------------------------')
print(f'4.2 performing difference operation symmetric_difference() method ')
difference = setI.symmetric_difference(setJ)
print('-----------------------------------------------------')
print(f'* Difference set I - J: {difference}')
elements = len(difference)
print('-----------------------------------------------------------------------------------------')
print(f'                   Currently the Symetric Difference Set I - J has: {elements} elements')
print('                  ---------------------------------------------------------------\n')

print('-------------------------------------')
print('5. Set Symetric Diference and Update ')
print('-------------------------------------\n')
# method finds the symmetric difference of two sets (non-similar items of both sets) 
# and updates it to the set that calls the method

setK = {28, 24, 90, 18}
setL = {24, 18, 79, 59}

print('-------------------------------------')
print(f'* Original Set K:  {setK} ')
print(f'* Original Set L:  {setL} ')
print('-------------------------------------')
elements = len(setK)
print(f' Currently the Set K has: {elements} elements')
elements = len(setL)
print(f' Currently the Set L has: {elements} elements')
print('-------------------------------------\n')

print('---------------------------------------------------------------------------')
print(f'5.1 performing difference operation symmetric_difference_update() method ')
symmetric_d = setK.symmetric_difference(setL)
setK.symmetric_difference_update(setL) # I cannot assign the updated set to a new variable
print('-----------------------------------------------------')
print(f'* Difference set K - L: {symmetric_d}')
print(f'* New Set: {setK}')
print('-----------------------------------------------------\n')

print('---------------------------------')
print('6. Check for equality of 2 sets ')
print('---------------------------------\n')
# We can use the == operator to check whether two sets are equal or not

setM = {24, 18, 16}
setN = {24, 18, 16}

print('-------------------------------------')
print(f'* Original Set M:  {setM} ')
print(f'* Original Set N:  {setN} ')
print('-------------------------------------')
elements = len(setM)
print(f' Currently the Set M has: {elements} elements')
elements = len(setN)
print(f' Currently the Set N has: {elements} elements')
print('-------------------------------------\n')

print('-----------------------------------------------------')
print(f'5.1 Check for Set Equiality')
print('-----------------------------------------------------')
if (setM == setN):
    print('------------------------------')
    print(f' Set M and Set N are Equals!')
    print(f' Set M {setM}')
    print(f' Set N {setN}')
    print('-----------------------------\n')
else:
    print('---------------------------------')
    print(f' Set M and Set N are Differents!')
    print(f' Set M {setM}')
    print(f' Set N {setN}')
    print('--------------------------------\n')
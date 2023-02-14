# ===================================================================
#  A dictionary is an ordered collection of items. 
#  It stores elements in key/value pairs. 
#  A keys are unique idenfifiers that are associated with each value
# ===================================================================


# ==================================================================================
#                                  CREATE A DICT

print('\t\t\t+---------------------+')
print('\t\t\t- CREATE A DICTIONARY -')
print('\t\t\t+---------------------+\n')


capital_city = {
    'United States of America': 'Washingtong',
    'Colombia': 'Bogota',
    'England': 'London'
}

print('1. Dictionary: ')
print('---------------------------------------------------------------------------------------')
print('* Capital City Dictionary:   ')
print(capital_city)
print('---------------------------------------------------------------------------------------\n\n')

week = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}

print('2. Dictionary with keys and values of different data types: ')
print('----------------------------------------------------------------------------------------------------')
print('* Days of the week:   ')
print(week)
print('----------------------------------------------------------------------------------------------------\n')

# =================================================================
#                  ACCESS DICTIONATY ELEMETNS 
# In python we use  the keys to acces their corresponding values

car_id = {1145: 'Mustang', 4511: 'Camaro', 4151: 'Jeep'}

print('3. Accessig Dictionary Elements: ')
print('------------------')
print(' Car Dictionary: ')
print('-------------------------------------------------')
print(car_id)
print('-------------------------------------------------')
print('* Accessing Key 4151:   ')
print(f'Value: {car_id[4151]}\n')
print('* Accessing Key 1145:   ')
print(f'Value: {car_id[1145]}')
print('-------------------------------------------------\n')

# =================================================================
#            ADD ELEMETNS TO A PYTHON DICTIONATY
#  We can add elements to a dictionary 
#  using the name of the dictionary with []

print('4. Adding Dictionary Elements: ')
print('------------------')
print(' Car Dictionary: ')
print('-------------------------------------------------')
print(car_id)
print('-------------------------------------------------')
print('* Add Cadilac:   ')
car_id[5141] = 'Cadilac'
print('-------------------------------------------------\n')

print('----------------------')
print(' New Car Dictionary: ')
print('----------------------------------------------------------------')
print(car_id)
print('----------------------------------------------------------------\n')


# =================================================================
#            CHANGE VALUE OF DICTIONARY
#  We can also use [] to change the values associated 
#  with a particular key

print('5. Changing Dictionary Values: ')
print('------------------')
print(' Car Dictionary: ')
print('----------------------------------------------------------------')
print(car_id)
print('----------------------------------------------------------------\n')
print('* Change Camaro to Ferrari:   ')
car_id[4511] = 'Ferrari'
print('----------------------')
print(' New Car Dictionary: ')
print('------------------------------------------------------------------')
print(car_id)
print('------------------------------------------------------------------\n')

# ===================================================================
#            REMOVE ELEMENTS FROM DICTIONARY
#  We use the del statement to remove an element from the dictionary

print('6. Removing Dictionary Elements: ')
print('------------------')
print(' Car Dictionary: ')
print('----------------------------------------------------------------')
print(car_id)
print('----------------------------------------------------------------\n')
print('* Delete Jeep from Dictionary:   ')
del car_id[4151]  
print('----------------------')
print(' New Car Dictionary: ')
print('------------------------------------------------------------------')
print(car_id)
print('------------------------------------------------------------------\n')

print('7. Delete the whole Dictionary: ')
print('------------------')
print(' Car Dictionary: ')
print('----------------------------------------------------------------')
print(car_id)
print('----------------------------------------------------------------\n')
print('* Delete Dictionary:   ')
del car_id  
print('----------------------')
print(' New Car Dictionary: ')
print('------------------------------------------------------------------')
print(car_id)
print('------------------------------------------------------------------\n')



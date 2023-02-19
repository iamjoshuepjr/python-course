# =================================================================
#                  Dictionary Membreship
#  We can test if a keu is in a dictionary or not using 
#  the keyword in. Membreship test 
#  is only for the keys and not for values

car_id = {
    1145: 'Mustang', 
    4511: 'Camaro', 
    4151: 'Jeep'
}

# membership test for dicts keys
isCar_id = 1145 in car_id
notInCar_id = 4511 not in car_id

# membership tests for key only not value
value = 'Camaro' in car_id

print(f'Id is in dict: {isCar_id}')
print(f'Id is not in dict: {notInCar_id}')
print(f'Testin values: {value}')
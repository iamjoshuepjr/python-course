# ===============================================================================
#  The all function retutns True if all elements in the given iterable are True. 
#  If not, it returns False.  
#  In the case of dictionaries, if all keys (not values) 
#  are true or the dictionary is empty returns True.

car_id = {
    1145: 'Mustang', 
    4511: 'Camaro', 
    4151: 'Jeep'
}

length = len(car_id)
print(f'Dictionary has {length} elements')


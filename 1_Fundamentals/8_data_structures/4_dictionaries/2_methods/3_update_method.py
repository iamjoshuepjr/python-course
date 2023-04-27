# =====================================================
#                   Update Method
#  The .update() method updates the dictionary with the
#  elements from another dictionary object or
#  from an iterable of key/value pairs.

print('\t\t\t+-----------------+')
print('\t\t\t- UPDATE() METHOD -')
print('\t\t\t+-----------------+\n')

print('\t\t\t+-------------------+')
print('\t\t\t- CREATE DICTIONARY -')
print('\t\t\t+-------------------+\n')

sport_cars = {
    1: 'Mazda MX-5 Miata',
    2: 'Saruba BRZ',
    3: 'Toyota GR86',
    4: 'Toyota Supra'
}

luxury_cars = {
    6: 'Ferrari',
    7: 'Lamborghini'
}

sport_cars.update(luxury_cars)
print(sport_cars)
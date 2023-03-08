# Ask for two values, then exchange them

a = int(input('Enter the first value: '))
b = int(input('Enter the second value: '))

print(f'You have entered: \nValue for a ({a}); value for b ({b})')

aux = a
a = b
b = aux 

print(f'New Values: \nValue for a ({a}); value for b ({b})')






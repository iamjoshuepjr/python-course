# Ask for two values, then exchange them

a = int(input('\nEnter the first value: '))
b = int(input('Enter the second value: '))

print(f'\nYou have entered: \nValue for a ({a}); value for b ({b})')

aux = a
a = b
b = aux 

print(f'\nNew Values: \nValue for a ({a}); value for b ({b})')
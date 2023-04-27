# Ask for tow number a dividen and a divisor, 
# and validate the operation will can be performed successfully

dividen = float(input('Enter a dividen number: '))
divisor = float(input('Enter a divisor number: '))

while divisor <= 0:
    print(f'Divisor {divisor} cannot must be a negative number: ')
    divisor = float(input('Enter another divisor: '))

division = dividen / divisor
print(f'Result: {division}')

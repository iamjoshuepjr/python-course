number1 = int(input('Enter a number here: '))
number2 = int(input('Enter another number here: '))

print(f'You had entered: {number1} and {number2}' +
       '\nSelect what operation you want to perform on them: ' +
       '\nAddition - (A - a)' +
       '\nSubtraction - (S -s)' +
       '\nMultiplication - (M -m)' +
       '\nDivision - (D -d)')

choice = input('Enter your choice here: ').lower()
match choice:
    case 'a':
        result = number1 + number2
    case 's':
        result = number1 - number2
    case 'm':
        result = number1 * number2
    case 'd':
        result = number1 / number2
    case _:
        result = f'Invalid ({choice}) choice'
print(f'Result: {result}')
def askNumber():
    while True:
        value = input('Enter a number: ')
        try:
            number = int(value)
            return number
        except ValueError as error:
            print(f'Error! [{value}] is not a number.')

numbers = []
print('Enter a number list\nZero to finish.')
while True:
    number = askNumber()
    if number == 0:
        break
    else:
        numbers.append(number)

print('What index you want to find?')
index = askNumber()

try:
    print(f'Element {numbers[index]} found! at [{index}] index')

except IndexError as error:
    print(f'Exception [{error}]')
    print(f'Index {index} not found!')
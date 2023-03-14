# Ask for a number, n, greater than 1 and adding the secuence from 1 until n

while True:
    number = int(input('Enter a number here: '))
    if(number > 1):
        break
    else:
        number = int(input(f'Number {number} is not greater than 1: '))
add = 0
for i in range(1, number+1):
    add += i
    if(i < number):
        print(f'{i}', end =', ')
    else:
        print(f'{i}')

print(f'Result: {add}')
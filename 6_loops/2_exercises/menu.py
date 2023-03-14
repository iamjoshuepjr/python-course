number1 = int(input('Enter a number here: '))
number2 = int(input('Enter another number here: '))
result = 0
option  = 0

while (option != 5):
    print(f'You had entered: {number1} and {number2}\nSelect what operation you want to perform on them: ')
    
    print('+----------------------+')
    print('-   Select an option   -')
    print('+----------------------+')
    print('- 1. Addition          -') 
    print('- 2. Subtraction       -') 
    print('- 3. Multiplication    -') 
    print('- 4. Division          -')
    print('- 5. Exit              -')
    print('+----------------------+')  

    option = int(input('\nEnter your option here: '))
    print('---------------------------')
    
    
    match option:
        case 1:
            result = number1 + number2    
        case 2:
            result = number1 - number2
        case 3:
            result = number1 * number2
        case 4:
            result = number1 / number2
        case 5:
            print('+----------------+')
            print('- See you later! -')
            print('+----------------+')
            break
        case _:
            result = 'Invalid Choosen!'

    print(f'\nYou had choosen {option}')
    print('---------------------------')
    print(f'\nResult: {result}')
    print('---------------------------')
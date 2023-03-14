print('\n------------------------------')
number1 = int(input(' Enter a number here: '))
number2 = int(input(' Enter another number here: '))
print('------------------------------\n')
result = 0
option  = 0

while (option != 5):
    print('+----------------------------------------------------')
    print(f'- You had entered: {number1} and {number2}\n- Select what operation you want to perform on them -')
    print('+----------------------------------------------------\n')

    print('+----------------------+')
    print('-   Select an option   -')
    print('+----------------------+')
    print('- 1. Addition          -') 
    print('- 2. Subtraction       -') 
    print('- 3. Multiplication    -') 
    print('- 4. Division          -')
    print('- 5. Exit              -')
    print('+----------------------+')  

    print('\n---------------------------')
    option = int(input('Enter your option here: '))
    print('---------------------------')

    def addition(x, y):
      return int (x + y)
    
    def subtraction(x, y):
      return int (x - y)
    
    def multiplication(x, y):
      return int (x * y)
    
    def division(x, y):
      return x / y
    def exit():
      return 'See you later!\nGood Hacking!'

    def default():
      return 'Invalid Selection!'

    match option:
      case 1:
        result = addition(number1, number2)
      case 2:
        result = subtraction(number1, number2)
      case 3:
        result = multiplication(number1, number2)
      case 4:
        result = division(number1, number2)
      case 5:
        result = exit()
      case _:
        result = default()
    
    print('+-----------------+')
    print(f'{result}')
    print('+-----------------+')
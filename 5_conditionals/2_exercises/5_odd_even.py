# Validate whether it a odd numeber or a even number
number = int(input('Enter the number here: '))
if(number % 2 == 0):
    print(f'Number entered ({number}) is even!')
else:
    print(f'Number entered ({number}) is odd!')
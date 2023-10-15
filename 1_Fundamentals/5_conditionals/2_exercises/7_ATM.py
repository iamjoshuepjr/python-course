import os

def clear_screen():
    os.system('clear')


def leave_app():
    exit_app = input('Do you want to leave the app?\nYour response: ')

balance = 10000
deposit, withdraw, currentBalance = 0, 0, 0


exit_app = 'n'
while exit_app == 'n':
    print('+------------------+')
    print('-  Welcome to ATM  -')
    print('+------------------+')
    print('- Select an option -') 
    print('- 1. Account       -') 
    print('- 2. Deposit       -') 
    print('- 3. Withdraw      -') 
    print('- 4. Exit          -')
    print('+------------------+') 
      
    choice = int(input('Enter your choice here: '))

    match choice:
        case 1:
            clear_screen()
            print('+----------------------------+')
            print(f'- Your Balance is $US {balance}  -')
            print('+----------------------------+')
            leave_app()
            clear_screen()
        case 2:
            clear_screen()
            deposit = float(input('Enter the deposit: '))
            currentBalance = balance + deposit
            print('\n+--------------------+')
            print('- Saved Successfully -')
            print('+--------------------+')
            leave_app()
            clear_screen()
        case 3: 
            clear_screen()
            withdraw = float(input('Enter the amount to withdraw: '))
            if(withdraw >  balance):
                print('\n+-------------------------------------------------+')
                print('- Invalid Action!\n- The amount to withdraw is greater thab balance. -')
                print('+-------------------------------------------------+')
            else:
                currentBalance = balance - withdraw
                print('+-------------------------------+')
                print(f'- New Balance: $US {currentBalance} -')
                print(f'- Withdraw: $US {withdraw} - ')
                print('+-------------------------------+')
                leave_app()
                clear_screen()
        case 4:
            clear_screen()
            print('+-----------------------------------+')
            print('- Thank you for using our services! -')
            print('+-----------------------------------+')
            leave_app()
            clear_screen()
        
        case _:
            clear_screen()
            print('+-------------------+')
            print('-     Warning!      -')
            print('- Invalid choice!   -')
            print('+-------------------+')
            leave_app()
            clear_screen()
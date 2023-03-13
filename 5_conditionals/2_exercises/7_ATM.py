balance = 10000
deposit, withdraw, currentBalance = 0, 0, 0

print('+------------------+')
print('-  Welcome to ATM  -')
print('+------------------+')
print('- Select an option -') 
print('- 1. Accoutn       -') 
print('- 2. Deposit       -') 
print('- 3. Withdraw      -') 
print('- 4. Exit          -')
print('+------------------+') 
      
choice = int(input('Enter your choice here: '))

match choice:
    case 1:
        print('+----------------------------+')
        print(f'- Your Balance is $US {balance}  -')
        print('+----------------------------+')
    case 2:
        deposit = float(input('Enter the deposit: '))
        currentBalance = balance + deposit
        print('\n+--------------------+')
        print('- Saved Successfully -')
        print('+--------------------+')
    case 3: 
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
    case 4:
        print('+-----------------------------------+')
        print('- Thank you for using our services! -')
        print('+-----------------------------------+')
        
    case _:
        print('+-------------------+')
        print('-     Warning!      -')
        print('- Invalid choice!   -')
        print('+-------------------+')
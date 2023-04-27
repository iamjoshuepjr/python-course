""" 
The try...except statement also has an optional clause called finally

try: 
   code that may cause exception
except: 
    code that handle exceptions  
finally:
    code that clean up
The finally clause always execites wheter an exception occurs or not. 
And it executes after the try clause amd any except clause.

"""
try:
    print('Enter two numbers: ')
    a = int(input('Enter a value for a: '))
    b = int(input('Enter a value for c: '))
    c = a / b
    print(f'Division {a}/{b} = {c}')
except ZeroDivisionError:
    print('I tried to divide by zero, but all I got was an existential crisis.') 
finally:
    print('Finishing up!')
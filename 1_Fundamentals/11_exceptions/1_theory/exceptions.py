# ========================================================================================
#                   Exceptions
# In Python, an exception is an error that occurs during program execution. 
# When an exception occurs the normal flow of the program is disrupted, 
# and the interpreter stops the execution of the program and generates an error message.
# The causes of exceptions mainly come from the enviroment wherw the code executes. 
# - Reading a file that doesn´t exist.
# - Connecting to a remote server that is offline.
# - Bad user inputs.
# Syntax 
#     try: 
#         code that may cause error
#     except:
#         handle errors

try:
    # get input net sales
    print('Enter the net sales for')
    previous = float(input('- Prior period: '))
    current = float(input('- Current period: '))

    # calculate the change in percentage
    change = (current - previous) * 100 / previous

    # show the result
    if(change > 0):
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)

except ValueError:    
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
except Exception as error:
    print(error)


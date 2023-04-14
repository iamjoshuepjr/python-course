# ===================================================
#                        ARGV
# In python 'ARGV' is a commonly used convention for 
# passing command line arguments to a Python script. 
# When you run a Python script from the commnand line 
# you can pass argumets to the script by appending them 
# after the script name. 
# For example: if you have a script called myscript.py 
# and you want to pass two arguments to it, 
# you can run the script like this:
# python myscript.py arg1 arg2

# =========================================================
# To access these arguments within your Python script, 
# you can use the sys.argv list. This list contains 
# the command line arguments passed to the script, 
# with the first argument (sys.argv[0]) being the name 
# of the script itself. 

import sys
if __name__ == "__main__":
    for argument in sys.argv:
        if argument == '-h' or argument == '--help':
            print('Welcome to this program!\n-a: addition\n-s: subtraction')
    print(sys.argv)
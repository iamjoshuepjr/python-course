# ====================================================================
#  Recursion is the process of  defining something in terms of itself 

# =========================================================
#  Python recursive function
#  Python function can call other functions, 
#  however, it's even posible for the function call itself

# Example 
def factorial(x):
    if (x == 1):
        return 1
    else:
        return (x * factorial(x -1))

num = 3
print(f'\nThe factorial of {num} is: {factorial(num)}\n')
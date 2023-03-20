# ===================================================
#                     Python Closures
# Python closure is a nested funtion that allows us 
# to access variables of the outer function even after 
# the function os closed. 

# define the outer function by passing a or any argument
def outer_function(x):
    # define the inner function by passing a or any argument
    def inner_function(y):
        # return computing
        return x + y
        # return the inner function
    return inner_function

# assing the outer function to a variable.
# when outer_function is called with an argument (x), 
# it returns inner_function, which is then assigned to the variable
closure = outer_function(10)
# so the inner_function is inside the variable, (variable 'becomes a function') 
# and it remembers the value of 'x' from outer_function
print(closure(14))

def validation(a, b):
    def validate():
        if((a > 0) and (b > 0)):
            return True
        else:
            return False
    return validate

closure = validation(9, 0)
print(closure())
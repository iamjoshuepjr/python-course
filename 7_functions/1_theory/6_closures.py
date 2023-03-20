# ===================================================
#                     Python Closures
# Python closure is a nested funtion that allows us 
# to access variables of the outer function even after 
# the function os closed. 

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print(outer_function(13))  # prints 13


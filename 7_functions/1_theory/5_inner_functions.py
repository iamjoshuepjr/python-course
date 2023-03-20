# =====================================================
# Inner Functions, also know as nested functions, 
# are functions that you define inside other functions. 
# In Python, this kind of functions has direct access 
# to variables and names defined in the enclosing function. 
# Inner functions have many uses, most notably as closures 
# factories and decoratos functions

def division(a, b):
    def validate():
        if((a > 0) and (b > 0)):
            return True
        else:
            return False
    if(validate() == True):
        return a // b
    else:
        return None

result = division(89, 9)
print(f'Result: {result}')
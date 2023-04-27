# Relational Operations Module

def equality(a, b):
    if(a == b):
        return f"The elements are equals!\nElement A [{a}] = Element B [{b}] "
    else: 
        return f"The elements are inequals!\nElement A [{a}] != Element B [{b}] "

def inequality(a, b):
    if(a != b):
        return f"The elements are inequals!\nElement A [{a}] != Element B [{b}] "
    else: 
        return f"The elements are equals!\nElement A [{a}] = Element B [{b}] "
        
def greaterThan(a, b):
    if(a > b):
        return f"The Element A [{a}] is greater than (>) Element B [{b}] "
    else:
        return f"The Element B [{b}] is greater than (>) Element A [{a}] "
    
def lessThan(a, b):
    if(a < b):
        return f"The Element A [{a}] is less than (<) Element B [{b}] "
    else:
        return f"The Element B [{b}] is less than (<) Element A [{a}] "
    
def greaterThanOrEqual(a, b):
    if(a >= b):
        return f"The Element A [{a}] is greater or equal to (>=) Element B [{b}] "
    else:
        return f"The Element B [{b}] is greater or equal to (>=) Element A [{a}] "

def lessThanOrEqual(a, b):
    if(a <= b):
        return f"The Element A [{a}] is less or equal to (<=) Element B [{b}] "
    else:
        return f"The Element B [{b}] is less or equal to (<=) Element A [{a}] "
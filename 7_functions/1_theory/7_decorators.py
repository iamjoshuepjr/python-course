# ==============================================
#                  Decorators
# A decorator is a function that takes another 
# functions as an argument and extends its behavior 
# without changing the original function explicity.
# The return of this function is a number. 
# Now, suppose that you need to format the net price using rthe USD currency. 
# For example 100 becomes $100. To do it, you can use a decorator.

#from functools import wraps

def currency(function):
    #@wraps
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f'USD ${result}'
    return wrapper

# To use the currency decorator, you need to pass the net_price function to it 
# to get a new function and execute the nre function as if it were the original function

# syntax to use the decorator
# shorter way
@currency
def net_price(price, tax):
    """
        Calculate the net price from net price and tax
        arguments:
            price: the selling price
            tax: value added tax or sale tax

        return:
            the net price
    """ 
    return price * (1 + tax)

print(net_price(100, 0.05))
# help(net_price)
# print(f'Decorator Name: {net_price.__name__}')

# When you decorate a function, you'll lose the origibal function signature 
# and documentation. To fix this, you can use the wraps function from the functools standard module.
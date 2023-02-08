# =================================================================================
#                            DETERMINE THE LENGTH OF A TUPLE
#  To get the length of a tuple, use the built-in function/method len(). 
#  The len() function/method find the number of elements present in a tuple.
#  The following code creates a new variable, months and week. 

print('\n\n\t\t\t\t    +----------------+')
print('\t\t\t\t    - CREATE A TUPLE -')
print('\t\t\t\t    +----------------+\n')


months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
week = ('Sunday', 'Monday', 'Tuesday', 'Wendnesday', 'Thursday', 'Friday', 'Saturday')

print('1. len() method')
print('---------------------------------------------------------------------------------------------------------------------------')
print('* Tuple having strings:   ')
print(months)
print(week)
print('---------------------------------------------------------------------------------------------------------------------------')
elements_month = len(months)
elements_week = len(week)
print(f'                             Currently the Months Tuple has: {elements_month} elements')
print(f'                             Currently the Week Tuple has: {elements_week} elements')
print('                           -------------------------------------------------\n')
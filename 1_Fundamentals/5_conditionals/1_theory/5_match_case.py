# The Match-Case is the Switch-Case of Python.
# Here we have to first pass a parameter then try to check with 
# case the parameter is getting satisfied. 
# If we find a match we will do something 
# and if there is no match at all we will do something else.

number = int(input('Enter the number of a day of the week: '))
day = ''
match number:
    case 1:
        day = 'Sunday'
    case 2:
        day = 'Monday'
    case 3:
        day = 'Tuesday'
    case 4:
        day = 'Wednesday'
    case 5:
        day = 'Thursday'
    case 6:
        day = 'Friday'
    case 7:
        day = 'Saturday'
    case _:
        day = 'Not valid day'
print(f'Day: {day}')
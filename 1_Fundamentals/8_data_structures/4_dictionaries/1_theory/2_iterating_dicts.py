# =================================================================
#                     Iterating through a dictionary 
#  We can iterate through each key in a dictionary usin a for loop

week = {
    1: 'Sunday', 
    2: 'Monday', 
    3: 'Tuesday', 
    4: 'Wednesday', 
    5: 'Thursday', 
    6: 'Friday', 
    7: 'Saturday'
}

print('\n------------------------------')
print('1. Iterating key Dictionaries: ')
print('------------------------------')
print('* Days of the week:   ')
for i in week:
    print(week[i])
print('\n------------------------------')
print('* Term and value:   ')
for term, value in week.items():
    print(f'Key: {term} - Value: {value}')
print('------------------------------')
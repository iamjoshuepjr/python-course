# =================================================================================
#                            DETERMINE THE LENGTH OF A SET
#  To get the length of a set, use the built-in function/method len(). 
#  The len() function/method find the number of elements present in a set.
#  The following code creates a new variable, months and week. 

print('\n\n\t\t\t\t\t+--------------+')
print('\t\t\t\t\t- CREATE A SET -')
print('\t\t\t\t\t+--------------+\n')

languages = {'Python', 'Java', 'JavaScript', 'C#', 'C++', 'Python'}
students_id = {100, 101, 102, 103, 104, 105, 106}

print('\n------------------------------------------------------------------------------')
print(f'* Original Students ID Set:   ')
print(students_id)
print(f'* Original Languages Set:   ')
print(languages)
print('------------------------------------------------------------------------------')
elements = len(students_id)
print(f'       Currently the Studens ID set has: {elements} element(s)')
elements = len(languages)
print(f'       Currently the Languages set has: {elements} element(s)')
print('------------------------------------------------------------------------------\n')
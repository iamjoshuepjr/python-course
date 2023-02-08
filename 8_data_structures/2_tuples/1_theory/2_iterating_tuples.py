# =================================================================
#                     Iterating through a Tuple 
#  We can use the for loop to iterate over the elements of a tuple

print('\n\n\t\t\t\t\t+----------------+')
print('\t\t\t\t\t- CREATE A TUPLE -')
print('\t\t\t\t\t+----------------+\n')

languages = ('Java', 'Python', 'C++', 'C#')

print('-------------------------------')
print('Languages tuple: ')
print(languages)
print('-------------------------------')
elements = len(languages)
print(f'                             Currently the Language Tuple has: {elements} elements')
print('                           ---------------------------------------------\n')

print('\t\t\t\t\t+-------------------+')
print('\t\t\t\t\t- ITERATING A TUPLE -')
print('\t\t\t\t\t+-------------------+\n')

for language in languages:
    print(f'Language: {language}')
print()

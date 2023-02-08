# =================================================================
#                     Iterating through a list 
#  We can use the for loop to iterate over the elements of a list

print('\n\n\t\t\t\t\t+----------------+')
print('\t\t\t\t\t- CREATE A LIST -')
print('\t\t\t\t\t+----------------+\n')

languages = ['Java', 'Python', 'C++', 'C#']

print('-------------------------------')
print('Languages List: ')
print(languages)
print('-------------------------------')
elements = len(languages)
print(f'                             Currently the Languages List has: {elements} elements')
print('                           ---------------------------------------------\n')

print('\t\t\t\t\t+------------------+')
print('\t\t\t\t\t- ITERATING A LIST -')
print('\t\t\t\t\t+------------------+\n')

for language in languages:
    print(f'Language: {language}')
print()
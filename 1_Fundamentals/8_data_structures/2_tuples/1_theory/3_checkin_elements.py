# =====================================================================
#                     Checking elemsnts in a Tuple 
#  We use the in keyword to check if an item exist in the tuple or not

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

print('\t\t\t\t\t+----------------------------------------+')
print('\t\t\t\t\t- CHECKING IF AN ITEM EXIST IN THE TUPLE -')
print('\t\t\t\t\t+----------------------------------------+\n')

language = input('Search languages: ')

if (language in languages):
    element = language 
    index = languages.index(element)
    print('--------------------------------------------')
    print(f'  The language ({language}) is in the tuple  ')
    print(f'  At the index [{index}]')
    print('--------------------------------------------')
else:
    print('-----------------------------------------------')
    print(f'The language ({language}) is not in the tuple')
    print('-----------------------------------------------\n')
# =====================================================================
#                     Checking elemsnts in a List
#  We use the in keyword to check if an item exist in the tuple or not

print('\n\n\t\t\t\t\t+--------------+')
print('\t\t\t\t\t- CREATE A LIST -')
print('\t\t\t\t\t+--------------+\n')

languages = ['Java', 'Python', 'C++', 'C#']

print('-------------------------------')
print('Languages List: ')
print(languages)
print('-------------------------------')
elements = len(languages)
print(f'                             Currently the Language List has: {elements} elements')
print('                           ---------------------------------------------\n')

print('\t\t\t\t\t+---------------------------------------+')
print('\t\t\t\t\t- CHECKING IF AN ITEM EXIST IN THE LIST -')
print('\t\t\t\t\t+---------------------------------------+\n')

language = input('Search languages: ')

if (language in languages):
    element = language 
    index = languages.index(element)
    print('--------------------------------------------')
    print(f'  The language [{language}] is in the list  ')
    print(f'  At the index [{index}]')
    print('--------------------------------------------')
else:
    print('-----------------------------------------------')
    print(f'The language [{language}] is not in the list')
    print('-----------------------------------------------\n')
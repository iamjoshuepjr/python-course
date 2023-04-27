# =====================================================
#                  
#  The sorted() function sorts the elements of a given 
#  iterable in a specific order (ascending or descending) 
#  and returns it as a list

vowels = {'e': 1, 'a': 2, 'u':3, 'o': 4, 'i':5}

print('\n-------------------------------------------')
print(f'* Original Vowel Dict:   ')
print(vowels)
print('\n-------------------------------------------')
print('\n            ---------------------------------------------')
elements = len(vowels)
print(f'             Currently the Vowels Dict has: {elements} element(s)')
print('            ---------------------------------------------')

print('\n\t\t\t    +-------------------------------+')
print('\t\t\t    -      SORTING THE DICT IN      -')
print('\t\t\t    -        ASCENDING ORDER        -')
print('\t\t\t    +-------------------------------+')

print('1 sorted() function')

vowel_list = sorted(vowels)

print('\n-----------------------------------------------------')
print(f'  The ascending order is: {vowel_list}')
print('-----------------------------------------------------\n')

print('\t\t\t    +-------------------------------+')
print('\t\t\t    -      SORTING THE DICT IN      -')
print('\t\t\t    -        DESCENDING ORDER       -')
print('\t\t\t    +-------------------------------+\n')

vowel_list = sorted(vowels, reverse = True)
print('1.1 sorted(reverse = True)')
print('\n-----------------------------------------------------')
print(f'  The descending order is: {vowel_list}')
print('-----------------------------------------------------\n')
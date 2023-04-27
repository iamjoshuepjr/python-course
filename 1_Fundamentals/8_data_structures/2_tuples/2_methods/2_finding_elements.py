# ====================================================================================
#                            FIND A VALUE IN A TUPLE
#  To determinate where in a tuple a value is stored, you use the tuple's index method
#  This method searches for the value and returns the index of that item in the tuple
#  If it doesn't find a match, it returns -1

print('\n\t\t\t\t   +---------------+')
print('\t\t\t\t   - CREATE A LIST -')
print('\t\t\t\t   +---------------+\n')

tech_companies = ('Apple', 'Netflix', 'Microsoft', 'Google', 'Amazon', 'Apple', 'Meta', 'Tesla', 'NVIDIA', 'Amazon', 'Meta', 'Samsung', 'Alibaba', 'Oracle', 'Netflix', 'Intel')

print('\n\t\t\t    +-------------------------------+')
print('\t\t\t    - FINDING INDEX OF THE ELEMENTS -')
print('\t\t\t    -             METHODS           -')
print('\t\t\t    +-------------------------------+\n')


print('1 .index() method')
# The .index() method can take a maximun of three arguments:
# element -> the elemenet to be searched
# start (optional) -> start searching from this index
# end (optional) -> search the element up to this index
to_find = input('Search company here: ')

if (to_find in tech_companies):
    element = to_find
    index = tech_companies.index(element)
    print('--------------------------------------------')
    print(f'  The Company ({to_find}) is in the tuple  ')
    print(f'  At the index [{index}]')
    print('--------------------------------------------')
else:
    print('--------------------------------------------')
    print(f'The Company ({to_find}) is not in the tuple')
    print('--------------------------------------------\n')


print('\n\t\t\t    +---------------------------------+')
print('\t\t\t    -  FINDING INDEX OF THE ELEMENTS  -')
print('\t\t\t    -  WITH START AND END PARAMETERS  -')
print('\t\t\t    +---------------------------------+\n')

element = 'Netflix' 
index = tech_companies.index(element, 3)
print('--------------------------------------')
print(f'  The index of the [{element}] is [{index}]')
print('--------------------------------------\n')

element = 'Meta'
index = tech_companies.index(element, 4, 11)
print('--------------------------------------')
print(f'  The index of the [{element}] is [{index}]')
print('--------------------------------------\n')

print('-------------------------------------------------------------------------------------------------------------------------------------')
print('* Tech Companies:   ')
print(tech_companies)
print('-------------------------------------------------------------------------------------------------------------------------------------')
elements = len(tech_companies)
print(f'                             Currently the Week Tuple has: {elements} elements')
print('                           -------------------------------------------------\n\n')

print('\t\t\t    +------------------------------+')
print('\t\t\t    - FINDING THE NUMBER OF ITEMS  -')
print('\t\t\t    -     APPEARS IN THE LIST      -')
print('\t\t\t    -           METHODS            -')
print('\t\t\t    +------------------------------+\n')

print('2. count() method')
# The count() method returns
# check the count of the element
element = 'Meta'
count = tech_companies.count(element)
print('--------------------------------')
print(f'({element}) appears {count} times')
print('--------------------------------\n')

element = 'Google'
count = tech_companies.count(element)
print('--------------------------------')
print(f'({element}) appears {count} times')
print('--------------------------------\n')

element = 'Twitter'
count = tech_companies.count(element)
print('--------------------------------')
print(f'({element}) appears {count} times')
print('--------------------------------\n')

element = 'Amazon'
count = tech_companies.count(element)
print('--------------------------------')
print(f'({element}) appears {count} times')
print('--------------------------------\n')

element = 'Netflix'
count = tech_companies.count(element)
print('--------------------------------')
print(f'({element}) appears {count} times')
print('--------------------------------\n')
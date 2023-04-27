# ========================================================
#    List Comprehension
#  Is a concise and elegent way to crate list
#  A list comprehension consist of an expression 
#  followed by the for estatement inside squares brackets

print('\n\n\t\t\t\t   +--------------------------+')
print('\t\t\t\t   - USING LIST COMPREHENSION -')
print('\t\t\t\t   +--------------------------+\n')

print('\t\t\t\t   +---------------------------------------+')
print('\t\t\t\t   - USING STRINGS WITH LIST COMPREHENSION -')
print('\t\t\t\t   +---------------------------------------+\n')

print('1. Iterating through a string Using for Loop\n')
word = 'Euphoria'
w_letter = []
for letter in word:
    w_letter.append(letter)
print(w_letter)    

print('\n2. List comprehension\n')
word = 'Aurora'
w_letter = [letter for letter in word]
print(w_letter)


print('\n\t\t\t\t   +------------------------------------+')
print('\t\t\t\t   - USING LIST WITH LIST COMPREHENSION -')
print('\t\t\t\t   +------------------------------------+\n')

print('\n1. Normal algoritm | Without list comprehension \n') 
numbers = []

for number in range(1, 6):
    numbers.append(number * number) 
print(f' List: {numbers}')

print('\n2. list comprehension\n')
numbers = [number * number for number in range(1, 6)]
print(f' List: {numbers}\n')

print('\n\t\t\t\t   +----------------------------------+')
print('\t\t\t\t   - USING IF WITH LIST COMPREHENSION -')
print('\t\t\t\t   +----------------------------------+\n')

print('1. Normal if statement (even numbers)')
even_numbers = []

for number in range (20):
    if (number % 2 == 0):
        even_numbers.append(number)
print(f' Even numbers: {even_numbers}')

print('\n2. If with list comprehension (odd numbers)\n')
odd_numbers = [number for number in range(20) if number % 2 == 1]
print(f' Odd numbers: {odd_numbers}')

print('\n3. Nested if (decenes)')
decene = []
for number in range(100):
    if (number % 2 == 0):
        if (number % 5 == 0):
            decene.append(number)
print(f' Decenes: {decene}')

print('\nNested Loops')
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(f'Transpose: {transposed}')

print('\nNested Loops in List Comprehension')
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
trasnpose = [[row[i] for row in matrix] for i in range(2)]
print(trasnpose)
print()
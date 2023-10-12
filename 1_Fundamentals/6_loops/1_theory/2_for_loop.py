# ===================================================
#  It has the ability to iterate over the items of
#  any sequence, such as a list or a string

# Syntax
# for iterator in sequence:
#     statements

# In Pyhton you can iterate practically everything
print()
print('Displaying Iteration with Python word')
print()
for letter in 'Python':
    print(f'Current Letter: {letter}') 

# output: letter -> take values for each letter in Python phrase
# P
# y
# t
# h
# o
# n

print()
print('Displaying Iteration with fruits list')
print('Way 1')
print()
# iterable
fruits = ['banana', 'apple', 'mango']
  # iterator  # iterable
for fruit in fruits:
    print(f'Current fruit: {fruit.title()}') #   .title == .capitalize()

print()
print('Displaying Iteration with fruits list')
print('Way 2')
print()
fruits = ['banana', 'apple', 'mango']
for fruit in range(len(fruits)):
    print(f'Current fruit: {fruits[fruit]}')

print()
print('Displaying Iteration with a specific range')
print('Way 3')
print()

for i in range(8):
        print(f"Number: {i+1}")
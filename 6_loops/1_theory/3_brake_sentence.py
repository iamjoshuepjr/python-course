# ===================================================
#           Break Statement
# This statement is used to terminate 
# the loop immediately when it's encountered

# Syntax: break

# We can use the break statement with the for loop to terminate it 
# when a certain condition is met
print()
print('+---------------------------+')
print('- Using the break statement -')
print('+---------------------------+')
print()
print('Values: ')
for i in range(24):
    if (i == 19): # when i is equal to 19
        nineteen = i
        break # the break statement terminates the loop
    print(i, end = ' ') # the output doesn't include values after 19

print('\n')
print('+------------------------------+')
print(f'- Break was applied to i == {nineteen} -')
print('+------------------------------+')
print('* After this value no number will be displayed ')
print()

# ===================================================
#                     More examples
print()
print('+------------------------------------------+')
print('- Find the first 6 multiples of any number -')
print('+------------------------------------------+')
print()

i = 1
n = int(input('Enter a number: '))
print()
print(f'The first 6 multiples of {n} are: ')
print()
while (i <= 10):
    print(f'{n} * {i} = {n * i}')
    if (i >= 6):
        break
    i += 1

print('\n\n')

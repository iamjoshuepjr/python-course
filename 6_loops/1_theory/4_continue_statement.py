# ============================================================================
#           Continue Statement
# This statement is used to skip the current iteration 
# of the loop, and the control flow of the program goes to the next iteration

# Syntax: continue

print()
print('+------------------------------+')
print('- Using the continue statement -')
print('+------------------------------+')
print()


# continue statement with the for loop 
for i in range(10):
    if (i == 6): # when i is equal to 19
        six = i # the continue statement skip the iteration
        continue
    print(i, end = ' ') # the output doesn't  the value 6

print()
print('+---------------------------------+')
print(f'- Continue was applied to i == {six} -')
print('+---------------------------------+')
print('* This value no will be displayed ')
print()

print()
print('+--------------------------------+')
print('- Print odd numbers from 1 to 10 -')
print('+--------------------------------+')
print('* Skiping the even numbers with continue statement\n')

# continue statement with the while loop
num = 0

while (num < 10):
    num += 1
    if (num % 2 == 0):
        continue
    print(num, end = ' ')
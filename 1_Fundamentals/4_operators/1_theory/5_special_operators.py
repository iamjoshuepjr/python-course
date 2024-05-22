# ==========================================================================================
#                                   Logical Operators
# In python 'is' and 'is not' are used to check if two values are located on the same part 
# of the memory. Two variables that are equal does not imply thay they are identical

# =====================================================
# Operator  |   Meaning       
#    is        True if the operands are identical 
#                   (refer to the same object) 
#   
#   is not     True if the operands are not identical 
#                   (don't refer to the same object)

five = 5
_five = 5

text1 = 'Python'
text2 = 'Python'

list1 = [24, 99, 56]
list2 = list1

list3 = [25, 17, 31]
list4 = [25, 17, 31]

print('\n\t\t    +---------------------------+')
print('\t\t    - "is" & "is not" Operators -')
print('\t\t    +---------------------------+\n')

print('\n\t\t      ------------------')
print('\t\t      - 1. is Operator -')
print('\t\t      ------------------\n')

print('----------------------------------')
print(f' {_five} is {five} ')
print(f' Result: {_five is five}\n')

print(f' {text1} is {text2} ')
print(f' Result: {text1 is text2}\n')

print(f' {list1} is {list2} ')
print(f' Result: {list1 is list2}\n')

print(f' {list3} is {list4} ')
print(f' Result: {list3 is list4}')
print('----------------------------------')

print('\n\t\t      ----------------------')
print('\t\t      - 2. is not Operator -')
print('\t\t      ----------------------\n')

five = 5
_five = 9

text1 = 'Python'
text2 = 'JavaScript'

list1 = [25, 17, 31]
list2 = [25, 17, 31]

print('--------------------------------------')
print(f' {_five} is not {five} ')
print(f' Result: {_five is not five}\n')

print(f' {text1} is not {text2} ')
print(f' Result: {text1 is not text2}\n')

print(f' {list1} is not {list2} ')
print(f' Result: {list1 is not list2}')
print('--------------------------------------')
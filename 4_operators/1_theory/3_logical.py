# ===========================================
#             Logical Operators
# This operator return booleans values


# ============================
#   AND Logical Operator
#     ONLY return True 
#  if a = True and b = True

print()
print("\t\t\t\t   +-------------------+")
print("\t\t\t\t   - LOGICAL OPERATORS -")
print("\t\t\t\t   +-------------------+")
print()

print('\t\t\t\t  +------------------------+')
print('\t\t\t\t  - (and) Logical Operator -')
print('\t\t\t\t  +------------------------+')
print()
a = True
b = False

result = a and b # False
print(f'a = [True] and b = [False]: [{result}]')

c = True
d = True 
result = c and d # True
print(f'c = [True] and d = [True]: [{result}]')

e = False
f = False
result = e and f
print(f'e = [False] and f = [False]: [{result}]')

# ============================
#    OR Logical Operator
#        return True 
#  if an operand is = True 

print()
print()
print('\t\t\t\t  +-----------------------+')
print('\t\t\t\t  - (or) Logical Operator -')
print('\t\t\t\t  +-----------------------+')
print()
g = True
h = False
result = g or h
print(f'g = [True] and h = [False]: [{result}]')

i = True
j = True
result = i or j
print(f'i = [True] and j = [True]: [{result}]')

k = False
l = False
result = k or l
print(f'k = [False] and l = [False]: [{result}]')

# ==============================
#    NOT Unary Logical Operator
#  Changes the boolean value
#        return True 
#  if an operand is = False 
#       and vice-versa

print()
print()
print('\t\t\t\t  +------------------------+')
print('\t\t\t\t  - (not) Logical Operator -')
print('\t\t\t\t  +------------------------+')
print()
m = True
n = False
result = not m
print(f'm = [True]  | so, not m = [{result}]')
result = not n
print(f'n = [False] | so, not n = [{result}]')
print()

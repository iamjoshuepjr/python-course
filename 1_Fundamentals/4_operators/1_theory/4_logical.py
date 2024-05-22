# ===========================================
#             Logical Operators
# This operator return booleans values

# ============================
#   AND Logical Operator
#     ONLY return True 
#  if a = True and b = True

print("\n\t\t\t\t   +-------------------+")
print("\t\t\t\t   - LOGICAL OPERATORS -")
print("\t\t\t\t   +-------------------+\n")

print('\n\t\t\t\t  +------------------------+')
print('\t\t\t\t  - (and) Logical Operator -')
print('\t\t\t\t  +------------------------+\n')

a = True
b = False

result = a and b # False
print(f'a = [{a}]  and b = [{b}]: [{result}]')

c = True
d = True 
result = c and d # True
print(f'c = [{c}]  and d = [{d}]:  [{result}]')

e = False
f = False
result = e and f # False
print(f'e = [{e}] and f = [{f}]: [{result}]')

# ============================
#    OR Logical Operator
#        return True 
#  if an operand is = True 

print('\n\n\t\t\t\t  +-----------------------+')
print('\t\t\t\t  - (or) Logical Operator -')
print('\t\t\t\t  +-----------------------+\n')

g = True
h = False
result = g or h
print(f'g = [{g}]  and h = [{h}]: [{result}]')

i = True
j = True
result = i or j
print(f'i = [{i}]  and j = [{j}]:  [{result}]')

k = False
l = False
result = k or l
print(f'k = [{k}] and l = [{l}]: [{result}]')

# ==============================
#    NOT Unary Logical Operator
#  Changes the boolean value
#        return True 
#  if an operand is = False 
#       and vice-versa

print('\n\n\t\t\t\t  +------------------------+')
print('\t\t\t\t  - (not) Logical Operator -')
print('\t\t\t\t  +------------------------+\n')

m = True
n = False
result = not m
print(f'm = [{m}]  | so, not m = [{result}]')
result = not n
print(f'n = [{n}] | so, not n = [{result}]\n')
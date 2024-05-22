# ====================================================
#         Comparison and relationals Operators
# This operators return booleans values

number1 = 24
number2 = 16

print(f"""\nNumbers:
     * Number1: {number1}
     * Number2: {number2}
      """)
# ====================================================
#         Equality and Inequality Operators

# Equality Operator (==)
result = (number2 == number1)
print(f'\nResult Equality Operator (==): \nIs \'{number2}\' equal to (==) \'{number1}\'?: {result}')

# Inequality Operator (!=)
result = (number2 != number1)
print(f'\nResult Inequality Operator (!=): \nIs \'{number2}\' inequal/different to (!=) \'{number1}\'?: {result}')

# ====================================================
#              Relationals Operators

# Greater than Operator (>)
result = (number2 > number1)
print(f'\nResult Greater than Operator (>): \nIs \'{number2}\' greater than (>) \'{number1}\'?: {result}')

# Less than Operator (<)
result = (number2 < number1)
print(f'\nResult Less than Operator (<): \nIs \'{number2}\' less than (<) \'{number1}\'?: {result}')

# Greater than or Equal to Operator (>=)
result = (number2 >= number1)
print(f'\nResult Greater than or Equal to Operator (>=): \nIs \'{number2}\' greater than or equal to (>=) \'{number1}\'?: {result}')

# Less than or Equal to Operator (<=)
result = (number2 <= number1)
print(f'\nResult Less than or Equal to Operator (<=): \nIs \'{number2}\' less than or equal to (<=) \'{number1}\'?: {result}\n')
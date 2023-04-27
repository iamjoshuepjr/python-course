print()
value = int(input("Enter a value between 0 - 5 here: "))

minValue = 0
maxValue = 5

result = (value >= minValue) and (value <= maxValue)
print(f'In range is: {result}. So {value} is in range {minValue} and {maxValue}')
result = (value <= minValue) and (value >= maxValue)
print(f'Out of range is: {result}. So {value} is in range {minValue} and {maxValue}')
print()
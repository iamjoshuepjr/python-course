# Write a Python Function to sum all the numbers in a list
def sumList(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(f'Sum: {sum((24, 20, 32, 10, 7))}')

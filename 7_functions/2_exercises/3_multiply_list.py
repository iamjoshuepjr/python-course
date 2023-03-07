# Write a Python Function to multiply all the numbers in a lists

def multiply (numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
print(multiply((2, 2, 3)))
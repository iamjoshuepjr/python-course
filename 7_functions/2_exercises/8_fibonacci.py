# Create 3 function to Fibonacci Numbers

# create a function to ask for a number and validate it be greater than 0
def askForNum():
    while True:
        num = int(input('Enter a positive number here: '))
        if(num > 0):
            return num

# create a function to order the fibonacci numbers
def fibonacci(num):
    numbers = []
    a = 0 
    b = 1 
    c = 0 
    
    for i in range(0, num):
        numbers.append(a)
        c = a + b
        a = b
        b = c
    return numbers

# create a function to display the fibonacci numbers 
def displayFibonacci(numbers):
    for number in numbers:
        if(number < numbers[-1]):
            print(f'{number}', end =', ')
        else:
             print(f'{number}')

displayFibonacci(fibonacci(askForNum()))
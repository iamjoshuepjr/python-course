# Create a function to ask for n numbers, then save them on a list. 
# Create a function to search for the greater and less numbers on the list.

# function to ask n numbers
def askForNum():
    numbers = []
    while True:
        number = int(input('\nPress 0 to exit!\nEnter a number here: '))
        if(number == 0):
            break
        else:
            numbers.append(number)
    return numbers
        
def searchFor(numbers):
    num_max = 0
    num_min = 9999
    for num in numbers:
        if(num > num_max):
            num_max = num
        if(num < num_min):
            num_min = num
    return num_max, num_min

greater, less = searchFor(askForNum())
print(f'Greater: ({greater}), Less: ({less})')
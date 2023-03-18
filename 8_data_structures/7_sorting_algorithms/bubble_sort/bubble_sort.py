# ===========================================================
# Bubble Sort is the simplest sorting  algorithm that works 
# by repeatedly swapping the adjacent elements of they are 
# in the wrong order. 
# This algorithm is not suitable for large data sets as 
# its average and worst-case time complexity is quite high

def askForNum():
    numbers = []
    while True:
        number = int(input('\nEnter 0 to exit.\nEnter a number here: '))
        if(number == 0):
            return numbers
        else:
            numbers.append(number)
    return numbers

def bubble(numbers):
    count = 0
    lenght = len(numbers)

    for _ in range(lenght):
        for j in range(0, lenght - 1):
            count += 1
            if(numbers[j] > numbers[j+1]):
                aux = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = aux 
    return numbers, count           

def diplayList(numbers, count):
    lenght = len(numbers)
    print(f'Ascending order in {count} times')
    for i in range(lenght):
        if (i < lenght -1):
            print(numbers[i], end = ", ")
        else:
            print(numbers[i])
    
    print(f'Descending order {count} times')
    for i in range(lenght, 0, -1):
        if (i > 1):
            print(numbers[i-1], end = ", ")
        else:
            print(numbers[i-1])
        
numbers = askForNum()
numbers, count = bubble(numbers)
diplayList(numbers, count)
# =============================================================================
#                         Insertion Sort
# Insert sort is a simple algorithm that works similar to the way you sort 
# playing cards in your hands. 
# The array is virtually split into a sorted and an unsorted part. 
# Values from the unsorted part are 
# picked and placed at the correct position in the sorted part.
# =============================================================================
#             Characteristics of Insertion Sort
# + This algorithm is one of the simplest algorithm with simple implementation
# + Basically, Insertion sort is efficient for small data values
# + Insertion sort is adaptive in nature, i.e., it is appropiate for data sets 
#   which already partially sorted.

def askForNum():
    numbers = []
    i = 0
    while True:
        number = int(input(f'\nEnter zero to finish.\nEnter the [{i}] number here: '))
        i+=1
        if(number == 0):
            return numbers
        else:
            numbers.append(number)


def insertionSort(numbers):            
    position = 0
    i = 0
    key = 0
    for _ in numbers:
        position = i
        key = numbers[i]
        while ((position > 0) and (numbers[position-1] > key)):
            numbers[position] = numbers[position-1]
            position -= 1
        numbers[position] = key
        i+= 1
    return numbers

def displayList(numbers):
    lenght =  len(numbers)
    i = 0
    for number in numbers:
        if (i < lenght - 1):
            print(number, end = ', ')
        else:
            print(number)
        i+=1
        

numbers = askForNum()
numbers = insertionSort(numbers)
print('\nAscending order with Insertion Sort: ')
displayList(numbers)
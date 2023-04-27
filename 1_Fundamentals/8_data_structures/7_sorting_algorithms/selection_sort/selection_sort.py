# ===========================================================================================
#                         Insertion Sort
# Selection sort is a simple and efficient sorting algorithm that works by 
# repeatedly selecting the smallest (or largest) element from the unsorted portion
# of the list and moving it to the sorted portion of the list.
# The algorithm repeatedly selects the smallest (or largest) element from the 
# unsorted portion of the list and swaps it with the first element of the unsorted portion. 
# This process is repeated for the remaining unsorted portion of the list 
# until the entire is sorted.
# One variantion of selection sort is called "Bidirectional Selection Sort" which goes through 
# the list of elements by alterating between the smallest and largest element, this way 
# the algorithm can be faster in some cases.
#
# The algorithm maintanins two subarrays in a given array.
# + The subarray which alerady sorted 
# + The remaining subarrays was sorted 
# 
# In every iteration of the selection sort, the minimum element (considering ascending order) 
# from the unsorted subarray is picked and moved to the beginning of the unsorted subarray. 
# After every iteration sorted subarray size increase by one and the unsorted subarray size decrease by one. 
# After the N (size of the array) iteration, we will get a sorted array.
# ===========================================================================================
#                          Characteristics of Insertion Sort

def askForNum():
    numbers = []
    i = 0
    while True:
        number = int(input(f'Enter the [{i+1}] number: '))
        if(number == 0):
            return numbers
        else:
            numbers.append(number)
        i += 1

def selectionSort(numbers):
    lenght = len(numbers)
    for i in range(0, lenght):
        minimum = i
        for j in range((i+1), lenght):
            if(numbers[minimum] > numbers[j]):
                minimum = j
        
        aux = numbers[i]
        numbers[i] = numbers[minimum]
        numbers[minimum] = aux
    return numbers
    
def displayList(numbers):
    lenght = len(numbers)
    i = 0
    for number in numbers:
        if (i < lenght - 1):
            print(number, end = ', ')
        else:
            print(number)
        i+=1

numbers = askForNum()
numbers = selectionSort(numbers)
print('\nAscending order with Insertion Sort: ')
displayList(numbers)
# ===================================================
#                   Binary Search
# Binary Search is a searching algorithm used in 
# a sorted array by repeatedly dividing the search 
# interval in half. The idea of binary search is to use 
# the information that the array is sorted and reduce 
# the time complexity to O(Log n)
# =========================================================================================
#                               Binary Search Algorithm
# + Sort the array in ascending order.
# + Set the low index to the first element of the array 
#   and the high index to the last element.
# + Set the middle index to the average of the low and high indices.
# + If the element at the middle index is the target element, return the middle index.
# + If the target element is less than the element at the middle index, set the high index 
#   to the middle index - 1
# + If the target element is greater than the element at the middle index, set the high index 
#   to the middle index + 1
# + Repeat steps 3 - 6 until the element is found or it is clear that the element 
#   is not present in the array
# ======================================================================
# Binary Search Algorithm can be implemented in the following two ways
# 1. iterative method
# 2. recursive method

def askForNum(numbers):
    lenght = len(numbers)
    i = 0
    for number in numbers:
        if(i < lenght - 1):
            print(number, end = ', ')
        else:
            print(number)
        i+= 1
    search = int(input('\nEnter the number you want to search for in the list: '))
    return search

def binarySearch(numbers, search):
    left = 0
    right = len(numbers) - 1
    position = 0
    while (left <= right):
        mid = (left + right) // 2
        if (numbers[mid] == search):
            position = mid
            return True, position
        elif (numbers[mid] < search):
            left = mid + 1
        elif (numbers[mid] > search):
            right = mid - 1
        position += 1
    return False, position
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    search = askForNum(numbers)
    found, position = binarySearch(numbers, search)
    if (found == True):
        print(f'Congrats!\nFound Number at [{position}] index - [{position + 1}] position')
        break
    else:
        print('Number no found!')
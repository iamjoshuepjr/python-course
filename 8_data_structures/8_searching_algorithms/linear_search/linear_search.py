# =============================================================================================
#                                      Linear Search
# Linear search is the simplest method for searching. In Linear search technique of searching;
# the element is searched sequentially in the list. This method can be performed on a sorted or
# an unsorted list (usually arrays)
# In case of a sorted list searching starts from 0th element and continues until the element is
# found from the list or the element whose value is greater than 
# (assumming the list is sorted in ascending order), the value being searched is reached.
# 
# As against this, searching in case unsorted list also begins from the 0th element and continues 
# until the element or the end of the list is reached. 

def askForNum(numbers):
    for number in numbers:
        print(number, end = ', ')
    search = int(input('\nEnter the number you want to search for in the list: '))
    return search

def linearSearch(numbers, search):
    for i in range(0, len(numbers)):
        position = 0
        if(search == numbers[i]):
            position = i
            return True, position
    return False

numbers = [81, 72, 63, 54, 45, 36, 27, 18]
while True:
    search = askForNum(numbers)
    found, position = linearSearch(numbers, search)
    if (found == True):
        print(f'Congrats! Found Number at [{position}] index - position[{position+1}]')
        break
    else:
        print('Number no found!')
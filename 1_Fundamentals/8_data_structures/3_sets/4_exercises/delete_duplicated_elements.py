list1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
print(list1)
'''
set1 = set()
set1 = set(list1)
list2 = list(set1)
print(set1)
list2.sort()
print(list2)
'''

list1 = list(set(list1))
list1.sort()
print(list1)
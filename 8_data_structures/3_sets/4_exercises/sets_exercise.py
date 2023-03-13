list1 = [2, 4, 6, 8, 10, 2, 4, 6]
list2 = [2, 3, 6, 9, 10, 3, 9, 2]

# deleting duplicated elements
print('Original List 1')
print(list1)
print('Original List 2')
print(list2)

print('New List 1')
list1 = set(list1)
print(list1)
print('New List 2')
list2 = set(list2)
print(list2)

# union
rs = list1 | list2
print(f'\nUnion - List 1 | List 2: {rs}')

# diference
rs = list1 - list2
print(f'\nDiference - List 1 - List 2: {rs}')
rs = list2 - list1
print(f'\nDiference - List 2 - List 1: {rs}')

# intersection
rs = list1 & list2
print(f'\nIntersection - List 1 & List 2: {rs}')
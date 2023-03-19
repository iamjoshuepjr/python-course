# Operations for lists 

def mixLists(arr1, arr2):
    newArr = []
    length1 = len(arr1)
    length2 = len(arr2)

    if (length1 >= length2):
        lengthGreater = length1
    else:
        lengthGreater = length2
    
    for i in range(0, lengthGreater):
        if(i < length1):
            newArr.append(arr1[i])
        if(i < length2):
            newArr.append(arr2[i])
    return newArr

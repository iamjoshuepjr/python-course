a = 0 # 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34
b = 1 # 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55
c = 0 # 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55

for i in range(1, 11, 1): # 10
    if(i < 10):
        print(a, end =", ")
        c = a + b
        a = b
        b = c
    else:
        print(a)
    # 0, 1, 1, 2, 3, 5, 7, 13, 21, 34
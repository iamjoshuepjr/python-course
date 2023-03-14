a = 0
b = 1
c = 0

for i in range(11):
    if(i < 9):
        print(a, end =", ")
        c = a + b
        a = b
        b = c
    else:
        print(a)
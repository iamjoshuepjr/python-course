# Read an integer, n, from STDIN.
# Without using any string methods try print the secuence from 1 to n

n = int(input())
for i in range(1, n+1):
    print(i, end = "")
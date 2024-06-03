# Create a python program to calculate if a year is a leap year

year = int(input("Enter the year here: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "Is a leap year!")
else:
    print(year, "Is not a leap year!")
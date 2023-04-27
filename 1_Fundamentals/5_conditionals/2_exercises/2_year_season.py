# ============================================================
# Exercise 2 
# Convert a month given as a number into the correct season

print()
month = int(input("Enter a month number to convert it to the season: "))
season = None
if((month == 12) or (month == 1) or (month == 2) or (month == 3)):
    season = "Winter Season"
elif ((month == 4) or (month == 5) or (month == 6)):
    season = "Spring Season"
elif ((month == 7) or (month == 8) or (month == 9)):
    season = "Summer Season"
elif ((month == 10) or (month == 11)):
    season = "Autumn/Fall Season"
else:
    season = "Season Out of Range"
    print()
print()
print("+------------------------------+")
print("- Month    |       Season      -")
print("+------------------------------+")
print(f"   {month}           {season} ")
print("+------------------------------+")
print()
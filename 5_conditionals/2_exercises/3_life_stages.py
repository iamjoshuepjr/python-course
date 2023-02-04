# ===============================================================
# Exercise 3 
# Convert an age given as a number into the correct life stage

print()
print("+----------------------------------------------+")
age = int(input(" Enter your age to display your life stage: "))
print("+----------------------------------------------+")

stage = None
if(age < 0):
    stage = "Waring!\nAge cannot be a negative number\nPlease, enter a positive number."
elif ((age > 0) and (age < 2)):
    stage = 'Infant'
elif ((age > 1) and (age < 5)):
    stage = 'Toddler' 
elif ((age > 4) and (age < 13)):
    stage = 'Child' 
elif ((age > 12) and (age < 20)):
    stage = 'Teen' 
elif ((age > 19) and (age < 40)):
    stage = 'Adult' 
elif ((age > 39) and (age < 60)):
    stage = 'Middle Age Adult' 
elif ((age > 59) and (age < 126)):
    stage = 'Senior Adult' 
else:
    stage = 'Next to die!' 

print()
print("+------------------------------+")
print("- Age    |     Life Stage      -")
print("+------------------------------+")
print(f"   {age}   |        {stage} ")
print("+------------------------------+")
print()
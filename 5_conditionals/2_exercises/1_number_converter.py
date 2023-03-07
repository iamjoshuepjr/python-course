# ==================================================
#   Exercise converter a given number into text

number = int(input('\nEnter a number between 1-3 you want to convert: '))
textNumber = ''

if (number == 1):
    textNumber = 'Number One'
elif (number == 2):
    textNumber = 'Number Two'
elif (number == 3):
    textNumber = 'Number Three'
else:
    textNumber = 'No valid value'
print(f"You have been entered: '{number}', which text value is: {textNumber}")
print()
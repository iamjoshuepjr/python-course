# =======================================================================================================
#  Sometimes there are more than tow possibiliies and we need more than two branches
#  One way to express a computation like that is a chained conditional
#  elif - is an abbreviation of "else-if"

print()
age = int(input('Enter your age here, please: '))

if(age < 0):
    print()
    print('Warning!\nYour age must not be a negative number!')
elif (age < 18):
    print()
    print('Warning!\nYou are not of legal age')
else:
    print()
    print('Congrats, you are of legal age')
print()
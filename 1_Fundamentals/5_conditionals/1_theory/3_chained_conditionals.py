# =======================================================================================================
#  Sometimes there are more than tow possibiliies and we need more than two branches
#  One way to express a computation like that is a chained conditional
#  elif - is an abbreviation of "else-if"

age = int(input('\nEnter your age here, please: '))

if(age < 0):
    print('\nWarning!\nYour age must not be a negative number!\n')
elif (age < 18):
    print('\nWarning!\nYou are not of legal age.\n')
else:
    print('\nCongrats, you are of legal age\n')
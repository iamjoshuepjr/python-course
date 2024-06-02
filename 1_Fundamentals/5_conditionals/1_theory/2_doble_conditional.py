# =======================================================================================================
#  The compound form: if-else conditional statement
#  This control structure allows us make-decitions depending the evaluation result:
#  There are tow possibilities (if - else) and the condition determines which one gets executed

age = int(input("\nEnter your age here, please: "))
if (age > 18):
    print("+--------------------------------+")
    print("  Congrats! You're of legal age!  ")
    print("+--------------------------------+")
else:
    print("+-------------------------+")
    print(" Sorry!\n You aren't of legal age! ")
    print("+-------------------------+\n")
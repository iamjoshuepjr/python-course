# ======================================================================================================
#  Ternary Operator
#  It's a compact alternative to the common multiline if-else control flow statements
#  in situations when you only need to "swicth" between tow values
#  test if a condition is true or false and, depending on the outcome, returns the corresponding value                   
#  All in just a line of code

age = int(input("Enter yourt age here, please: "))
print("Congrats\nYou are of legal age!") if (age >= 18) else print("Warning!\nYou aren't of legal age!")
# ====================================================================================
#  The simplest form: if simple conditional statement
#  The boolean expresion after the if statement is called the condition          
#  This control structure allows us make-decitions depending the evaluation result:
#  If it's true, then the idented statement gets executed. If not, nothing happens

print("The simplest conditional statement")
age = int(input("Enter your age here: "))
if(age > 18):
    # Actions for True
    print("You are a young person.")
# Input - Output  
  

# input function -> allow us get from user by standar input values to process
# this methos only get str
name = input("Enter your name here: ")
age = int(input("Enter your age here: "))
birthday = input("Enter your birthday (dd/mm/yyyy): ")
ip = input("Enter your IP here: ")
print()
print("\t+-----------------------+")
print(f"\t Name {name}")
print(f"\t Age: {age}")
print(f"\t Birthday: {birthday}")
print(f"\t IP: {ip}")
print("\t+------------------------+")

print()
print("+----------------------------+")
print(" [Good - Regular - Bad]      ")
result = input(" How was your day?  ")
print(f" Your day was: {result}     ")
print("+----------------------------+")
print()
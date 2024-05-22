# Input - Output  
  
# input function -> allow us get from user by standar input values to process
# this methods only get str
name = input("Enter your name here: ")
age = int(input("Enter your age here: "))
birthday = input("Enter your birthday (dd/mm/yyyy): ")
ip = input("Enter your IP here: ")
height = float(input('Enter your hight in meters: '))

print("\n\t+-----------------------+")
print(f"\t Name {name}")
print(f"\t Age: {age}")
print(f"\t Birthday: {birthday}")
print(f"\t Height: {height} meters")
print(f"\t IP: {ip}")
print("\t+------------------------+\n")

print("+----------------------------+")
print(""" 
    Provide a feedback about your day
      + Good
      + Regular
      + Bad """)
result = input(" How was your day?  ")
print(f" Your day was: {result}     ")
print("+----------------------------+\n")
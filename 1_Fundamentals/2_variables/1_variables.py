# Variables
# Allows store data

# ==================================================================================
#                 Assign values to variables 
# The equal (=) operator allows us to assign a value to a variable

# varName: str ->  indicates reference to the data type
variable: str = "Hello, from Python!"
print(f"variable: {variable}")

# varName: int ->  indicates reference to the data type
variable: int = 24
print(f"variable: {variable}")

# varName: float ->  indicates reference to the data type
variable: float = 24.99
print(f"variable: {variable}")

# varName: int ->  indicates reference to the data type
x: int = 24
y: int = 21
z: int = x + y 
print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

# ==================================================================================
#                        multiple assignment 
# You can to assign a single value to several variables

a = b = c = 24
print(f"Assigned to a: {a}")
print(f"Assigned to b: {b}")
print(f"Assigned to c: {c}")

# You can also assign multiple objects to multiple variables
a, b, c =  24, 1, "Joshuép Jr."
print(f"New Value Assigned to a: {a}")
print(f"New Value Assigned to b: {b}")
print(f"New Value Assigned to c: {c}")

# =====================================================================================================
#                       functions with variables 
# the function id() allows us to know the memory address in which the value of the variable is stored

print(f"Memory id for x:", id(x))
print(f"Memory id for y:", id(y))
print(f"Memory id for z:", id(z))
# 1 season - Data Types    

# varName: int        -> indicates reference to the data type we using (but no define it)
# the type() function -> allows us to know the data type of the variable
# the id() funtion    -> allows us to know the memory address in which the value of the variable is 

# int
print()
age: int = 24
print("+-----------------------------------+")
print("-          Int Data Type            -")
print("+-----------------------------------+")
print(f"  Variable value: {age}")
print(f"  Data type:, {type(age)}")
print(f"  Memory address:, {id(age)}")
print("+-----------------------------------+\n")
        
# float
decimal: float = 24.99
print("+-----------------------------------+")
print("-         Float Data Type           -")
print("+-----------------------------------+")
print(f"  Variable value: {decimal}")
print(f"  Data type: {type(decimal)}")
print(f"  Memory address: {id(decimal)}")
print("+-----------------------------------+\n")

# string (str)      
text: str = "Python"
print("+-----------------------------------+")
print("-         String Data Type          -")
print("+-----------------------------------+")
print(f" Variable value: {text}")
print(f" Data type:", {type(text)})
print(f" Memory address: {id(text)}")
print("+-----------------------------------+\n")

# boolean  (True - False)    
decision = True
print("+-----------------------------------+")
print("-        Boolean Data Type          -")
print("+-----------------------------------+")
print(f" Variable value: {decision}")
print(f" Data type: {type(decision)}")
print(f" Memory address: {id(decision)}")
print("+-----------------------------------+\n")

decision2 = False
print("+-----------------------------------+")
print("-        Boolean Data Type          -")
print("+-----------------------------------+")
print(f" Variable value: {decision2}")
print(f" Data type:", {type(decision2)})
print(f" Memory address: {id(decision2)}")
print("+-----------------------------------+\n")
# create a program that converts temperature 
# from Celsius to Fahrenheit and vice versa.

celsius = float(input("Enter your celsius grades here: "))
fahrenheit = float(input("Enter your fahrenheit grades here: "))

to_celsius = (fahrenheit - 32) * 5/9
to_fahrenheit = (celsius * 9/5) + 32

print(f""" 
      The result
      *
      * Before Celsius = {celsius}° | After Celsius converted F° {to_fahrenheit}
      * Before Fahrenheit = {fahrenheit}° | After Fahrenheit converted C° {to_celsius}
      """)
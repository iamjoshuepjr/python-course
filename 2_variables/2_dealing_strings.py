rockSpanish = "Morat"
rockEnglis = "Linkin Park"
genderMusic = "Rock"

# Warning!
# concatenation aint the same than addition
print()
print("-----------------------------------------------")
print("-  DIFFERENT WAYS TO DISPLAY A CONCATENATION  -")
print("-----------------------------------------------")
print()
# form 1 (+ sign) 
print("------------------------------------------------")
print("My favorite band in Spanish is " + rockSpanish)
# form 2 (, sign)
print("My favorite gender is:", genderMusic)
# form 3 (f"{}") format
print(f"My favorite band in English is: {rockEnglis}")
print("------------------------------------------------")

# Simple concatenation
a = "1"
b = "2"
print(f"Concatenation: '1' + '2' = {a+b}")
print("---------------------------------------")

# Casting str to int
a = "1"
b = "2"
print(f"Casting from str to int '1' + '2' = {int(a)+int(b)}")
print("---------------------------------------")

a = 1
b = 2
print(f"Simple addition: {a+b}")
print("---------------------------------------")
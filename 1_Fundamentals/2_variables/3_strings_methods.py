# Strings Methods
print()
print('\t\t\t\t    +-----------------+')
print('\t\t\t\t    - STRINGS METHODS -')
print('\t\t\t\t    +-----------------+')
print()
print()

print('.lower() method')
# lower() method -> converts a string into lower case
lower = "THIS TEXT IS IN UPPERCASE LETTERS, SO WITH THE LOWER() FUNCTION, IT WILL BECOME LOWERCASE."
print(f'Original Text: {lower}')
# it'll print: this text will become lower case.
print(f'Text Applied .lower() method: {lower.lower()}')
print()

# upper() method -> converts a string into upper case
print('.upper() method')
upper = "This text is in lowercase letters, so with the upper() function, it will become uppercase."
print(upper.upper())
# it'll print: THIS TEXT WILL BECOME UPPER CASE

#capitalize() method -> converts the firts character to upper case
print()
capitalize = "this text will be capitalized."
print(capitalize.capitalize())
# it'll print: This text will be capitalized

# strip() method -> delete the blank spaces
strip = "            Deleting blank spaces..."
print(strip.strip())
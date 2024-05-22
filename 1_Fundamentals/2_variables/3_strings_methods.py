# Strings Methods

print('\n\n\t\t\t\t    +-----------------+')
print('\t\t\t\t    - STRINGS METHODS -')
print('\t\t\t\t    +-----------------+\n\n')

print('.lower() method')
# lower() method -> converts a string into lower case
lower = "THIS TEXT IS IN UPPERCASE LETTERS, SO WITH THE LOWER() FUNCTION, IT WILL BECOME LOWERCASE."
print(f'Original Text: {lower}')
# it'll print: this text will become lower case.
print(f'Text Applied .lower() method: {lower.lower()}\n')

# upper() method -> converts a string into upper case
print('.upper() method')
upper = "This text is in lowercase letters, so with the upper() function, it will become uppercase."
print(f'Original Text: {upper}')
print(f'Text Applied .lower() method: {upper.upper()}\n')
# it'll print: THIS TEXT WILL BECOME UPPER CASE

#capitalize() method -> converts the firts character to upper case
print(".capitaliza() method")
capitalize = "this text will be capitalized."
print(f"Original text: {capitalize}")
print(f"Text Applied .capitalize() method: {capitalize.capitalize()}\n")
# it'll print: This text will be capitalized

# strip() method -> delete the blank spaces
print(".strip() method")
strip = "            Deleting blank spaces..."
print(f"Original text: {strip}")
print(f"Text Applied .strip() method: {strip.strip()}")
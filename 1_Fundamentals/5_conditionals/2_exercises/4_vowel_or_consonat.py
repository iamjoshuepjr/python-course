# Ask for a letter and determine whether it is a vowel or consonant

letter = input('Enter a letter: ').lower()

if((letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u')):
    print('The letter you have entered is a vowel')
else:
    print('The letter you have entered is a consonant')

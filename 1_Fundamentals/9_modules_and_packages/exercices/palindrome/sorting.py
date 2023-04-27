def palindrome(text):
    text = text.replace(' ', '')
    length = len(text)
    count = 0
    for i in reversed(range(0, length)):
        if ((text[i].lower()) != (text[count].lower())):
            return False
        count += 1
    return True

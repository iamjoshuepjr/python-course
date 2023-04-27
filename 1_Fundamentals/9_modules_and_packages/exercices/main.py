import mixing_lists.operations as mix
import palindrome.sorting as sorting
from lambda_functions.arithmetic import addition

even = [1, 3, 5, 7, 9]
odd = [2, 4, 6, 8, 10, 12, 14]

print(mix.mixLists(even, odd))

while True:
    text = input('\nEnter a palindrome here: ')
    isPalindrome = sorting.palindrome(text)
    if(isPalindrome == True):
        print(f'The text [{text}] is a palidrome!')
        break
    else:
        print(f'The text [{text}] is not a palidrome!')

print(f'Add Result: {addition(23, 9)}')
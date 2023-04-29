""" 
 =======================================
  Open file for reading in Binary mode
 =======================================
"""
print('* Move to the 5th character')

with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'rb') as file:
    # move the file handle to the 5th character
    file.seek(5)
    # read 24 bytes and convert it to string
    print(file.read(24).decode('utf-8'))

    # move the file handle 10 points from the current position
    file.seek(10, 1)
    # read 24 bytes and convert it to string
    print(file.read(24).decode('utf-8'))


""" 
 ===================================================================
             Seek backward with negative offset
 ===================================================================
 In some cases, we have to read characters from the end of the file.
 To do that, we need to move the file pointer in a reverse direction. 
"""

print('* Move to the 10th character')
# Move the 10th character from the end of the file
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'rb') as file:
    # move in reverse direction
    file.seek(-40, 2)
    # read 24 bytes and convert it to string
    print(file.read(24).decode('utf-8'))

print('* Move in reverse position')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'rb') as file:
    print(file.read(24).decode('utf-8'))
    # move in reverse direction
    file.seek(-5, 1)
    print(file.read(24).decode('utf-8'))
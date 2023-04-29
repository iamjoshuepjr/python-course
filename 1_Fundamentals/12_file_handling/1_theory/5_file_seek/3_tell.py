""" 
 =============================================
  tell() function to get file handle position
 =============================================
"""
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'r+') as file:
    # moving the file handle to the end of the file
    file.seek(0, 2)

    # getting the file handle position
    print(f'file handle at: {file.tell()} position.')

    # wrinting new content
    file.write('\nDemostrating tell')

    # getting the file handle position
    print(f'file handle at: {file.tell()} position.')

    # move to the beginning
    file.seek(0)

    # getting the file handle position
    print(f'file handle at: {file.tell()} position.')

    print('\n+----------------------+\
          \n- Printing file content\
          \n+----------------------+')
    print(file.read())
    print('\n+------+\
          \n- Done! -\
          \n+-------+')
    
    # getting the file handle position
    print(f'file handle at: {file.tell()} position.')
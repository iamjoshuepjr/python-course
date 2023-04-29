""" 
 =====================================================================
                        seek()
 =====================================================================
 The seek() funcion sets the position of a file pointer and the tell()
 function returns the current position of a fil pointer. A file handle 
 or pointer denotes the position from which the file contents will be 
 read or written. Sometimes we may have to read only a specific 
 portion of the file, in such cases use the seek() method to move the 
 file pointer to that position.
 Syntax:
 f.seek(offset, whence)
 =================================================================
  Seek Operation                Meaning 
 ================================================================= 
 f.seek(0)        Move file pointer to the beginning of a file              
 
 f.seek(5)        Move file pointer five characters ahead from 
                  the beginning of a file.
 
 f.seek(0, 2)     Move file pointer to the end of a file.

 f.seek(5, 1)     Move file pointer five characters ahead from the 
                  current position.
 
 f.seek(-5, 1)    Move file pointer five characters behing from the
                  current position.
 
 f.seek(-5, 2)    Move file pointer in reverse direction. Move it to 
                  the 5th character from the end of the file.                     
"""

with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'r') as file:
   print(file.read())
   print('------------')

with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'r') as file:
   file.seek(6) # It means we will start reading the file directly from the 6th character
   print(' Seek(6)')
   print('------------')
   print(file.read())
   print('------------')

# seek the beginning of the file
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'w+') as file:
   # adding
   file.write('\nSeventh Line')
   file.write('\nEighth Line')
   file.seek(0) # It means we will start reading the file directly from the 6th character
   print(' Seek(0)')
   print('------------')
   print(file.read())

# seek the beginning of the file
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\2_empty.txt', 'r+') as file:
    # moving the file pointer to the end 
    print('\n----------------------------------------\
           \n Seek(0, 2) \'the end\' to add new content\
           \n---------------------------------------')
    file.seek(0, 2)
    # writing
    file.write('\nThis content is added to the end of the file.')
    # read
    print(file.read())

    print('\n----------------------------------------------------------\
           \n Seek(0) \'the beginning\' to view the whole file content\
           \n---------------------------------------------------------')
    # moving to the begining and read the whole file
    file.seek(0)
    print(file.read())
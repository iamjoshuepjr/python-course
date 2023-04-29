"""
 ===============================================================
                 Read a file in Python
 =============================================================== 
 Temporary data that is locally used in a module will be stored 
 in a module will be stored in a variable. In large volumes of 
 data, a file is used such as text and CSV files and there are 
 methods in Python to read or write data in those files.
 ===============================================================
   File mode                Meaning 
 =============================================================== 
 r               The default mode for opening a file to read the 
                 contents of a text file. 
                 
 r+              Opens a file for both rading and writing. 
                 The file pointer will be placed at the beginning
                 of the file. 
                 
 
 rb              Opens the file for reading in a binary format. 
                 The file pointer will be placed at the beginning 
                 of the file.
 
 w+              Opens a file for both writing as well as reading. 
                 The file pointer will be placed at the beginning 
                 of the file. For an existing file, the content will 
                 be overwritten.
 
 a+              Opens a file for both reading and appening. 
                 The file pointer will be placed at the end 
                 of the file. For an existing file, the content will 
                 be overwritten.

 =============================================
      Steps for opening file in Python
 ============================================= 
 1. Find the path of a file
 2. Open the file in read mode
 3. Read the content from a file
 4. Close file after completing operation                 

 =============================================
 1. Reading a file using the 'with' statement
 =============================================
 We can open a file using the with statement 
 along the open function. The general sintax
 is as follows: 
                      Syntax:
 with open(__file__, access_mode) as __new_name__:
""" 
print('+-------------------------\
     \n- Reading the whole file -\
     \n+-------------------------\n')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
   print(file.read())

print('+--------------------------------\
     \n- Reading n bytes from the file -\
     \n+--------------------------------\n')

try:
  file = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r')
  print(file.read(107))
except FileNotFoundError:
  print('Please check the path!')
finally:
  file.close()

print('+---------------------------------------\
     \n- Reading and writing to the same file -\
     \n+---------------------------------------\n')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r+') as file:
   print(file.read())
   file.write('\nNew content')
   print(file.read())
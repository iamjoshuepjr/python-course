"""
 ===============================================================
                 Open a file in Python
 =============================================================== 
 The data can be in the from of files such as text, csv, 
 and binary files. To extract data from these files, Python comes 
 with built-in functions to open a file and them read and write 
 the file's content.

 ===============================================================
   File mode                Meaning 
 =============================================================== 
 r               Opens a file for reading (default) 
                 
 w               Opens a file for writing. If the file already 
                 exists, it deletes all the existing contents and
                 adds new content from the start of the line.
 
 x               Creates a file for exclusive creation. If the file 
                 already exists, this operation fails.
 
 a               Opens a file a file in the append mode and add 
                 new content at the end of the file.

 b               Opens a binary file.

 t               Opens a file in a text mode (default)
 
 +               Opens a file for updating (reading and writing).
"""

"""
 ===============================================================
              Steps for opening file in Python
 =============================================================== 
 1. Find the path of a file
 2. Decice the access mode
 3. Add file path and access mode to the open() function
 4. Read content into the file
 5. Write content into the file
 6. Close file after completing operation
"""
# =============================
# 1. Openig a file in read mode
# =============================
data_file = open(r'1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\1_write.txt', 'r')
# reading file
print(data_file.read())

# closing after reading
data_file.close()

# =============================
# 2. Openig a file in read mode
# =============================
try:
  file = open(r'1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\2_write.txt', 'r')
  print(file.read())
except FileNotFoundError:
  print('Please check the path.')
finally:
  file.close()

# ==============================================================
#             3. Openig a file in append mode
# ==============================================================
# We can append some content at the end of the file using 
# the open() function by passing the character a as the 
# access mode. The cursor will be placed at the end of the file 
# and the new content will get added at the end. 

# The difference between this and the write mode is that the 
# file's content will no be truncated or deleted in this mode.

try:
  file = open(r'1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'a')
  file.write('\n| 1. Open file with \'a\' mode.   |')
  
  # now opening file to read it
  file = open(r'1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\1_write.txt', 'r')
  print(file.read())
  file.close()
except FileNotFoundError:
  print('Please check the path.')

# ==============================================================
#             4. Openig file using with statement 
# ==============================================================
# We can open a file using the with statement along with the 
# open function. 
# The general syntax is as follows:
# with open(file, accessmode) as name

with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\1_write.txt', 'a') as file:
  file.write('\n| 2. Open file with \'with\' statement. |')
  file.write('\n| 3. Adding more content |')

file = open(r'1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\3_write.txt', 'r')
print(file.read())
file.close()

# ==============================================================
#            5. Openig file for multiples operations 
# ==============================================================
# In Python, we can open a file performing multiple operations 
# simultaneously by using the '+' operator. When we pass 'r+' mode 
# then it will be enable both rading and writing options in the file.

with open(r'1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r+') as file:
  # read before writing
  print(file.read())

  # writing
  file.write('\n| 2. Adding more content with \'r+\'. |')
              
  # read before writing
  print(file.read())
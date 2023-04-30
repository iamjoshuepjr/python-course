"""
 ===============================================================
                 Create an empty text file 
 =============================================================== 
 We don't have to import any module to create a new file. We can
 create a file using the built-in function open()
 Syntax:
 open('file_path', 'access_mode')

 ===============================================================
   File mode                Meaning 
 =============================================================== 
 x            Creates a file for exclusive creation. If the file
              already exists, this operation fails, and an error 
              will be raised. 
 
 w            Used to create and write content into a new file.
              create a new file for writing. If already exists, 
              it truncates the file first. 

 a            Opens a file in the append mode and add new content
              at the end of the file.
 
 b            Creates a binary file a file in the append mode 
              and add new content

 t            Creates and open a file in a text mode.                
"""
import os
# =============================
# 1. create an empty text file
# =============================
def ask():
  name = input('File name: (test.txt): ')
  mode = input('File mode: (w, x): ')
  return name, mode

def emptyfile():
    print('\n+----------------------+\
           \n- Create an empty file -\
           \n+----------------------+\n')
    root = '1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\'
    name, mode = ask()
    path = root + name
    try:
        data_file = open(path, mode)
    except Exception as e:
        print(e)
    finally:
        data_file.close()
        
emptyfile()

# ============================
# 2. create and write a file
# ============================
def createwrite():
  print('\n+-------------------------+\
         \n- Create and Write a file -\
         \n+-------------------------+\n')
  root = '1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\'
  name, mode = ask()
  path = root + name
  try:
    data_file = open(path, mode)
    data_file.write('| 1. create and write a file |')
    
  except Exception as e:
    print(e)
  finally:
    data_file.close()

createwrite()

"""
 ===============================================================
              Create a file in a specific directory
 =============================================================== 
 To create a file inside a specific directory, we need to open 
 a file using (absolute/relative) path.
 create a file using the built-in function open()
 Syntax:
 open('file_path', 'access_mode')
"""

# ============================
# 3. create and write a file
# ============================

directory = r"1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\"
name = '2_write.txt'
path = os.path.join(directory, name)

"""
  =========================================================
   Using the with statement a file is closed automatically 
   it ensures that all the resources that are tied up with 
   the file are released.
  =========================================================
"""

with open(path, 'w') as file:
  file.write('| 2. create and write a file |')
    
""" 
 ===============================================================
                        Verify the result
 ===============================================================
"""
# list files from a working directory
print('files inside 1_empty Directory:' , os.listdir(r"1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty"))
print('files inside 2_write Directory:' , os.listdir(r"1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write"))
# verify file exist
print(f'Is 2_write.txt in the Directory? ', os.path.isfile(r"1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\2_write.txt"))
"""
 ===============================================================
                 Create an empty text file 
 =============================================================== 
 We don't have to import any module to create a new file. We can
 create a file using the built-in function open()
 Syntax:
 open('file_path', 'access_mode')
"""
# =============================
# 1. create an empty text file
# =============================
data_file = open(r'13_file_handling\\1_theory\\1_create_files\\files\\1_empty_file.txt', 'x')
data_file.close()

# ============================
# 2. create and write a file
# ============================
data_file = open(r'13_file_handling\\1_theory\\1_create_files\\files\\2_create_write_file.txt', 'w')
data_file.write('+----------------------------+\
                 \n| 2. create and write a file |\
                 \n+----------------------------+')
data_file.close()

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
import os
# ============================
# 3. create and write a file
# ============================
dir_path = r'13_file_handling\\1_theory\\1_create_files\\files\\'
file_name = '3_create_write_file.txt'
file_path = os.path.join(dir_path, file_name)

"""
 =========================================================
  Using the with statement a file is closed automatically 
  it ensures that all the resources that are tied up with 
  the file are released.
 =========================================================
"""
with open(file_path, 'w') as file:
    file.write('+----------------------------+\
              \n| 3. create and write a file |\
              \n+----------------------------+')
    
""" 
 ===============================================================
                        Verify the result
 ===============================================================
"""
# list files from a working directory
print('files inside my_files Directory:' , os.listdir(r"13_file_handling\\1_theory\\1_create_files\\files"))
# verify file exist
print('Is file_3.txt in the directory? ', os.path.isfile(r"13_file_handling\\1_theory\\1_create_files\\files\\2_create_write_file.txt"))
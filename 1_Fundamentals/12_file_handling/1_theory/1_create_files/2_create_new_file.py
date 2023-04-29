"""
 ============================================================================
                 Create a new file if doesn't exist 
 ============================================================================ 
 Sometimes it is essential not create a new file if a file with the same 
 name already exists in a given path. By default, when  you open a file 
 in write mode, it overwrites it if it exists, else create the new one.
 We can create a file only if it's not present using the following two ways:
 1. Use os.path.exist("file_path") function to check if a file exists
 2. Use the access mode x in the open() function to check if a file exists
"""

# ==================================
# 1. create file if does not exist
# ==================================
import os
file_path = r'1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\3_write.txt'
if os.path.exists(file_path):
    print('File already exists!')
else:
    # create a file
    with open(file_path, 'w') as file:
        file.write('| 3. Create a new file if doesn\'t exist. |')

# ==========================
# 2. Use file access mode x
# ==========================
try: 
    file_path = r'1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\3_write.txt'
    # create file
    with open(file_path, 'x') as file:
        pass
except:
    print('File already exists!')
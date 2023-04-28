"""
 ============================================================================
                 Create a file with permission 
 ============================================================================ 
 + To create a file with appropiate permissions, use the os.open() to create 
   the file descriptor and set the permission.
 + Next, open the descriptor using the built-in function open()
"""
import os

file_path = '1_Fundamentals\\12_file_handling\\1_theory\\1_create_files\\files\\2_write\\6_permission_file.txt'
# the default umask is 0o22 which turns off write permission of group and others
os.umask(0)
with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as file:
    file.write('+-----------------------------------------+\
              \n| 6. Create a new file with permissions.  |\
              \n+-----------------------------------------+')
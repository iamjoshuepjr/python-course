# ==============================================
#       Pathlib module to remove file
# ==============================================
# The pathlin module offers clases representing 
# filesystem paths with semantics appropiate for 
# different operating systems. Thus, whenever we 
# need to work with files in multiple enviroments, 
# we can use the pathlib module.

import pathlib, os, shutil
# setting the path for the file
file = pathlib.Path('1_Fundamentals\\12_file_handling\\1_theory\\files\\5_delete\\5_delete.txt')
# calling the unlike method on the path
try:
    file.unlink()
    print('Done! File deleted.')
except FileNotFoundError:
    print('No longer file in path.')


# =======================================================
#         Delete all files from a directory 
# ========================================================
# Sometimes we want to delete all files from a directory

try:
    path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\5_delete\\'
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print(f'Deleting file: {file}')
            os.remove(file)
except Exception:
    print('No longer folder in path.')

# =======================================================
#        Delete an empty directory rmdir()
# ========================================================
# Sometimes there are empty folders that no longer needed.
# We can delete them using the rmdir() method available in 
# both os module and the pathlib module.

try:
    directory = '1_Fundamentals\\12_file_handling\\1_theory\\files\\5_delete\\'
    os.rmdir(directory)
    print(f'Deleted directory {directory} successfully!')
except FileNotFoundError:
    print('No longer folder in path.')

# way 2
try:
    directory = '1_Fundamentals\\12_file_handling\\1_theory\\files\\5_to_delete\\'
    path = pathlib.Path(directory)
    path.rmdir()
    print('Deleted directory successfully!')
except FileNotFoundError:
    print('No longer folder in path.')


# =====================================================================
#        Delete an non-empty directory shutil()
# =====================================================================
# Sometimes we need to delete a folder and all files contained in it.
# Use the rmtree() of shutil module. This module helps performing 
# high-level operations in a file or collection of files like copying
# or removing content.

try:
    directory = '1_Fundamentals\\12_file_handling\\1_theory\\files\\6_to_delete\\'
    shutil.rmtree(directory, ignore_errors=True)
    print('Deleted directory successfully!')
except FileNotFoundError:
    print('No longer folder in path.')
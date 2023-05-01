"""
 =====================================================================
                   Shutil Methods
 =====================================================================
    Shutil module offers many high-end functions to perform copy 
    and removal of files. 
    These functions provide an optimized way to copy files and there 
    by save time on performing unnecessary task of opening, reading, 
    writing and closing the files when there is no processing required in 
    that file.
"""

import shutil, os
from shutil import SameFileError

# ================================================================================
#  The shutil.copyfile() is used to copy the contents of one file to another file. 
#  The metadata of the file will not be copied.
# ================================================================================

source_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_copy\\'
destination_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\2_copy\\'

print(f'Destination folder before copying:\
    \n{os.listdir(destination_folder)}')

# file names
source_file = source_folder + 'file_2.txt'
destination_file = destination_folder + 'copied_file_2.txt'

try:
    # copy file
    shutil.copyfile(source_file, destination_file)
    print('Copied File!')
    print(f'Destination folder after copying: \
         \n{os.listdir(destination_folder)}')
except SameFileError:
    print('We are trying to copy the same file')
except IsADirectoryError:
    print('The destination is a directory')


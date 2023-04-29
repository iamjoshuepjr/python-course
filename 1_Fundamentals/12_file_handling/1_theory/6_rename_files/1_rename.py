""" 
 =============================================
                Rename files 
 =============================================
"""
import os 

old_name = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\1_rename.txt'

try: 
    file_path = old_name
    # create file
    with open(file_path, 'x') as file:
        pass
except FileExistsError:
    print('File already exists!')

# # rename 
new_name = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\2_rename.txt'
try:
    os.rename(old_name, new_name)
    print('Done!')
except FileExistsError:
    print('You cannot create a file already existing!')

""" 
 ================================================
  Rename a file after checking whether it exists
 ================================================
"""

old_name = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\1_rename.txt'
new_name = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\2_rename.txt'

if os.path.isfile(new_name):
    print('The file already exists!')
else:
    # rename it
    os.rename(old_name, new_name)

try: 
    os.rename(old_name, new_name)
except FileExistsError:
    print('File already exists')
    print('Removing existing file.')
    # remove it
    os.remove(new_name)
    # rename it 
    os.rename(old_name, new_name)
    print('Done renaming a file!')
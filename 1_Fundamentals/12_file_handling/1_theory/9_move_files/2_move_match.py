# =====================================================================
#                             Move match
# =====================================================================

import glob, os, shutil

# try: 
#     source = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\1_copy\\'
#     destination = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_folder\\'

#     pattern = '\*.txt'

#     files = glob.glob(source + pattern)

#     for file in files:
#         name = os.path.basename(file)
#         shutil.move(file, destination + name)
#         print(f'Moved: {file}')

# except FileNotFoundError: 
#     print('1. No such file or directory.')  


# =====================================================================
#                       Move files based on filename
# =====================================================================

source = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\2_copy'
destination = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\2_folder\\'

# move file whose name starts with string 'copied'
pattern = source + '\\account*'
for file in glob.iglob(pattern, recursive=True):
    # extract file name from file path
    name = os.path.basename(file)
    shutil.move(file, destination + name)
    print(f'Moved: {file}')
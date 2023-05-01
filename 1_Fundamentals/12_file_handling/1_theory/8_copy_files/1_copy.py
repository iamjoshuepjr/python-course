# =====================================================================
#                     Copy a file
# =====================================================================
# We can copy single and multiple files using different methods and 
# the most commonly used one is the suhtil.copy()

import shutil, os

try:
    src_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\6_copy\\copy_file_1.txt'
    dst_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\4_new_rename\\copy_file_1.txt'
    shutil.copy(src_path, dst_path)
    print('Copied!')
except Exception:
    print('Could not find this file!')

# # =====================================================================
# #                   Copy a all files from a directory
# # =====================================================================

try:
    source_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\6_copy\\'
    destination_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\4_new_rename\\'

    # fetch all files
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # copy only files
        if os.path.isfile(source):
            shutil.copy(source, destination)
            print(f'Copied {file_name}')
except Exception:
    print('Could not find this file!')

# =====================================================================
#                   Copy entire directory
# =====================================================================
# If the destination folder already exist, an error will be raised, so 
# make sure to choose a destination folder that doesn't already exist.

try:
    source_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\'
    destination_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\'
        
    shutil.copytree(source_folder, destination_folder)

except FileExistsError:
    print('Cannot create a file when that file already exists.')
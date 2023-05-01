# =====================================================================
#                     Copy a file an
# =====================================================================
# We can copy single and multiple files using different methods and 
# the most commonly used one is the suhtil.copy()

import shutil, os

src_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\6_copy\\copy_file_1.txt'
dst_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\4_new_rename\\copy_file_1.txt'
shutil.copy(src_path, dst_path)
print('Copied!')

# =====================================================================
#                   Copy a all files from a directory
# =====================================================================
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



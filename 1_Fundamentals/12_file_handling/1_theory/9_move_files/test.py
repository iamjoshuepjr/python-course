import os, shutil

# =====================================================================
#                   Move multiple files
# =====================================================================


source = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\1_copy\\'
destination = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_folder\\'
to_move = ['file_1.txt', 'file_4.txt']

# iterate files
for file in to_move:
    # construct full file path
    new_source = source + file 
    new_destination = destination + file 
    # move file
    shutil.move(new_source, new_destination)
    print(f'Moved: {file}')
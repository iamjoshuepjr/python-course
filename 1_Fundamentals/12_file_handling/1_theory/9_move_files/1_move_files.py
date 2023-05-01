# =====================================================================
#                     Copy a file
# =====================================================================
# We can move files using the shutil.move() method.

import shutil, os

try:
    source_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_copy.pdf'
    destination_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\1_copied.pdf'

    shutil.move(source_path, destination_path)
    print('Done! The file has been moved.')
except FileNotFoundError: 
    print('1. No such file or directory.')

# =====================================================================
#                     Move file and rename
# =====================================================================
try:
    source = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\2_copy\\'
    destination = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\'
    file = 'copied_file_1.txt'

    # check if file exist in destination
    if os.path.exists(destination + file):
        # split name and extension
        data = os.path.splitext(file) # ('2_copied_file_1', '.txt')
        only_name = data[0] # 2_copied_file_1
        extension = data[1] # .txt
        # adding the new name
        new_base = only_name + '_new' + extension #2_copied_file_1_new.txt
        # construct fill file path
        new_name = os.path.join(destination, new_base) 
        # move file
        shutil.move(source + file, new_name)
        print('Done! The file has been moved.')
    else:
        shutil.move(source + file, destination + file)
        print('Done! The file has been moved.')

except FileNotFoundError: 
    print('2. No such file or directory.')

# =====================================================================
#                   Move all files from a directory
# =====================================================================

try: 
    source = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_folder\\'
    destination = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\1_copy\\'

    # fetch all files
    for file in os.listdir(source):
        new_source = source + file
        new_destination = destination + file

        # move only files
        if os.path.isfile(new_source):
            shutil.move(new_source, new_destination)
            print(f'Moved: {file}')
        else:
            print('No found file.')        
except FileNotFoundError: 
    print('3. No such file or directory.')        


# =====================================================================
#                   Move multiple files
# =====================================================================
source = '1_Fundamentals\\12_file_handling\\1_theory\\files\\8_copied\\1_copy\\'
destination = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_folder\\'
to_move = ['file_1.txt', 'file_4.txt']

try:
    # iterate files
    for file in to_move:
        # construct full file path
        new_source = source + file 
        new_destination = destination + file 
        # move file
        shutil.move(new_source, new_destination)
        print(f'Moved: {file}')

except FileNotFoundError: 
    print('4. No such file or directory.')
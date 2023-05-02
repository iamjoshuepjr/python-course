# =============================================
#          List Files in a Directory
# =============================================
# There a multiple ways to list of directory. 

import os, pathlib, glob
# way 1
# folder path
dir_path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_folder'

# list to store files
result = []

# iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        result.append(path)
print('\n7_copy/1_folder files:')        
print(result)

# way 2
def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
path =  '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\1_folder'

print('\n7_copy/1_folder files:')        
for file in get_files(path):
    print(file)

# way 3
path =  '1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\'
print('\n2_write folder files:')        
for path in os.scandir(path):
    if path.is_file():
        print(path)

# way 4
path =  '1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\'
print('\n2_write folder files: ')
result = os.listdir(path)
print(result)
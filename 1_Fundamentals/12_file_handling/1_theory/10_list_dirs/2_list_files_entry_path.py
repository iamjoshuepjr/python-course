import glob, pathlib

# way 1
# folder path
path =  '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\2_folder'

# to store files names
result = []

# construct path object
destination = pathlib.Path(path)

# iterate directory
for entry in destination.iterdir():
    # check if it a file
    if entry.is_file():
        result.append(entry)
print('\n7_copy/2_folder entry relative path files:')        
print(result)

# way 2
# search all files inside a specific folder
# *.* means file name with any extension

print('\n2_write folder entry relative path files:')        
path =  '1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\*.*'
files = glob.glob(path)
print(files)


import os
from os import walk

# folder path
path =  '1_Fundamentals\\12_file_handling\\1_theory\\files\\7_copy\\'

# list to store files name
result = []

for (path, folders, files) in walk(path):
    result.extend(files)

print(result)
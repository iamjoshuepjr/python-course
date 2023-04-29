"""
 ========================================================
                 Rename multiple files in python
 ========================================================= 
 Sometimes we need to rename all files from a directory. 
 We can rename multiple files in a folder using 
 the os.rename() method by following the below steps:
 
 + get the list a files in a directory: using os.listdir() 
   it returns a list containing the names of the entries
   in the given directory.

 + iterate over the list using a loop to access each file 
   one by one
 
 + Rename each file
"""
import os
folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\'
count = 1
# count increase by 1 in ecah iteration; iterate all files from a directory
for file_name in os.listdir(folder):
    # construc old file name
    source = folder + file_name

    # adding the count to the new file name and extension
    destination = folder + str(count) +'_renamed' + '.txt'

    # renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are (rename all files): ')
result = os.listdir(folder)
print(result)
print('+----------------------------------------------------+')

"""
 ========================================================
        Renaming only a list of files in a folder
 ========================================================= 
 While renaming files insie a folder, sometimes we may to 
 rename only a list of files, not all files.
 Steps to ranaming only a set of files inside a folder:
 
 + providing the list of files that needs to be renamed.
   
 + iterate through the list of files in the folder 
   containing the files
 
 + check if the files is present in the list
   - if present, rename the file acording the desired 
     convention, else, move to the next file.
"""
import os
files_to_rename = ['1_renamed.txt', '3_renamed.txt']

for file in os.listdir(folder):
  # checking if the files is present in the file
  if file in files_to_rename:
    # contruct current name using file name and path
    old_name = os.path.join(folder, file)
    # get file name wihtout extension
    only_name = os.path.splitext(file)[0]

    # adding the new name with extension
    new_base = only_name + '_new' + '.txt'
    # construct full file path
    new_name = os.path.join(folder, new_base)

    # renaming base
    os.rename(old_name, new_name)

print('New Names are (rename a set of files): ')
result = os.listdir(folder)
print(result)
print('+----------------------------------------------------+')
"""
 ============================================================
                 Rename files with a Pattern
 ============================================================ 
 We can change only the extension of the files using rename(). 
 This is done by getting the list of the files and then get 
 only the file name using the splitext() of the os module
 This method returns the root and extension separately. 
 Once we get the root/base of the filename, we can add the new 
 extension to it while renaming it using the rename()
 
 Steps:
 + get list file names from a directory using os.listdir(folder)
 + next, iterate each file from a list of filenames
 + construct current file name using os.path.join() by passing file
 + now, use the replace() of a str class to replace an extension
 + at last, use the os.rename() to rename an old name with a new one
""" 

import os

folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\'
# listing the files of a folder
print('Before rename')
files = os.listdir(folder)
print(files)

for name in files:
    # construct the full file path
    old_name = os.path.join(folder, name)

    # changing the extension from txt to pdf
    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)

print('After rename')
print(os.listdir(folder))

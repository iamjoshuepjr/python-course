"""
 ============================================================
                 Rename files with a Pattern
 ============================================================ 
 With the help of the rename() we can rename a file and then 
 move it to a new location. This is done by passing the new 
 location to the rename() method's dst parameter. 
""" 
import glob, os
# old and new folder location
old_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\'
new_folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\4_new_rename\\'

# olde and new names
old_name = old_folder  + 'expense.txt'
new_name = new_folder  + 'expense.txt'

# moving the file to the another location
os.rename(old_name, new_name)

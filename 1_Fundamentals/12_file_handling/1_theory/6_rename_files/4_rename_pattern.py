"""
 ========================================================
                 Rename files with a Pattern
 ========================================================= 
 Sometimes we wanted to rename only those files that math 
 a specific pattern. For example, renaming only pdf files 
 or renaming files containing a particular year in their 
 name. The pattern matching is done using the glob module. 
 The glob module is used to fing the files and folders 
 whose names follow a specific patter. 
 We can rename files that match a patter using the followig 
 steps:
 
 + write a pettern using wildcard characters
 + use a glob() method to find the list of files that 
   matches a pattern
 + iterate through the files in the folder
 + change the name according to the new naming convention
"""
import glob
import os

path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\'

# search text files starting with the word 'file' 
pattern = path + 'file' + '*.txt'

# list of the files that match the pattern
pattern_result = glob.glob(pattern)

# iterating the list with the count
count = 1
for file in pattern_result:
  old_name = file
  new_name = path + str(count) + '_revenue' + '.txt'
  os.rename(old_name, new_name)
  count += 1

pattern_result = glob.glob(path + 'revenue' + '*.txt')
for name in pattern_result:
  print(name)
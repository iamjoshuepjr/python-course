"""
 ============================================================================
                    Renaming files with timestamp
 ============================================================================ 
 In some applications, the data or logs will be stored in the files regulary 
 in a fixed time interval. It's a standar convention to append a timestamp to 
 file name to make them easy for storing and using later. 
 We can use the datetime module to work with dates and times.
 
 Steps to append timestamp to file name:
 + get the current timestamp using a datetime module and store it in a 
   separate variable
 
 + convert timestamp into a string

 + append timestamp to file name using the concatenation operator
 + Now, rename a file with a new name using os.rename()
"""
import os
from datetime import datetime

try: 
    folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\'
    path = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\6_file.txt'
    # create file
    with open(path, 'x') as file:
        pass
except:
    print('File already exists!')

# adding date-time to the file name
current_timestamp = datetime.today().strftime('%d-%b-%Y')
old_name = r'1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\7_file.txt'
new_name = r'1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\7_file' +current_timestamp+ '.txt'

result = os.listdir(folder)
print('Folder Before')
print(result)

os.rename(old_name, new_name)
print('Folder After')
result = os.listdir(folder)
print(result)



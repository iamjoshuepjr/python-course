"""
 ============================================================================
                     Create a File with DataTime 
 ============================================================================ 
 Let's see how to create a text file with the current data as its name. 
 Use the datatime module to get the current data and time and assign it to 
 the file name to create a file with the data time in its name.
"""
from datetime import datetime
import os
# get current date and time
current = datetime.now()

# create a file with date as a name day-month-year
dir_path = "1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\"
file_name = current.strftime('4_%d-%m-%Y.txt')
file_path = os.path.join(dir_path, file_name)

with open(file_path, 'w') as file:
    print('created', file_name)

# create a file with name as day-month-year-hours-minutues-seconds
dir_path = "1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\"
file_name = current.strftime('5_%d-%m-%Y-%H-%M-%S.txt')
file_path = os.path.join(dir_path, file_name)
with open(file_path, 'w') as file:
    print('created', file_name)
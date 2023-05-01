""" 
 ====================================================
                Delete files and directories
 ====================================================
 Sometimes we need to delete files from a directory 
 that is no longer needed. Also, after some time, 
 the application needs to delete its old log files.

 =================================================================================
   Funtion                                           Meaning 
 ================================================================================= 
  os.remove('file_path')                     Removes the specified file 
              
  os.unlink('file_path')                     Removes the specified file. 
                                             Useful in UNIX enviroment

  pathlib.Path('file_path').unlink()         Delete the file or symbolic
                                             link in the mentioned path
 
  os.rmdir('empty_dir_path')                 Removes the empty folder

  pathlib.Path('empty_dir_path').rmdir()     Unlink and delete the empty folder 
"""
import os 

directory = '1_Fundamentals\\12_file_handling\\1_theory\\files\\5_delete\\'
name = '7_delete.txt'
path = os.path.join(directory, name)

try:
    with open(path, 'w') as file:
        file.write('| 7. create a file to delete it |')
        print(f'Done! {name} created.')
except Exception as e:
    print(e)

file_del = '1_delete.txt'
remove = os.path.join(directory, file_del)
os.remove(remove)
print(f'Done! {file_del} deleted.')

"""
 ========================================
 check if file exist before deleting it
 ========================================
 A FileNotFounderError will be raised if 
 the file is not found in the path.

 This can be achived in two ways:
 + os.path.exists('file_path') function
 + exception handling
"""

file_del = '2_delete.txt'
remove = os.path.join(directory, file_del)
if os.path.exists(remove):
   os.remove(remove)
   print(f'Done! {file_del} deleted.')
else:
   print(f'The system cannot find the file ({file_del}) specified!')

file_del = '3_delete.txt'
remove = os.path.join(directory, file_del)

try:
  os.remove(remove)
  print(f'Done! {file_del} deleted.')
except:
  print(f'The system cannot find the file ({file_del}) specified!')


# ==============================================
#     Remove file using os.unlink()
# ==============================================
# The os.unlink() is similar to the os.remove() 
# except that it is more familiar in the UNIX 
# enviroment


file_del = '4_delete.txt'
remove = os.path.join(directory, file_del)

try:
  os.unlink(remove)
  print(f'Done! {file_del} deleted.')
except:
  print(f'The system cannot find the file ({file_del}) specified!')
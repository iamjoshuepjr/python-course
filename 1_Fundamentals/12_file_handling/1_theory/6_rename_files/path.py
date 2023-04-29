import os

folder = '1_Fundamentals\\12_file_handling\\1_theory\\files\\3_rename\\'
files_to_rename = ['4_renamed.txt', '5_renamed.txt']

for file in os.listdir(folder):
  # checking if the file is present in the file
  if file in files_to_rename:
    # contruct current name using file name and path
    old_name = os.path.join(folder, file)
    # get file name wihtout extension
    only_name = os.path.splitext(file)[1]

    # adding the new name with extension
    new_base = only_name + '_new' + '.txt'
    # construct full file path
    new_name = os.path.join(folder, new_base)

    # renaming base
    os.rename(old_name, new_name)

result = os.listdir(folder)
print(result)


# Input/Output Python File Operation

# =========================================================================
#  A file is a container (a collection of data stored on a disk in one unit
#  identified by filename) in computer storage devices used for storing data 
#  temporarily and permanently. 
#  When we want to read from or write to a file, we need to open it first. 
#  When we was done, it needs to be closed so that the resources that are 
#  tied with the file are freed. 
#  Hence, in Python, a file operation takes place in the following order:
#  1. Open a file 
#  2. Read or write (perform operation) 
#  3. Close the file

# ===============================================================
#                        Types of files
# =============================================================== 
# + Text file: Text file usually we use to store character data.
# + Binary file: We use them to store binary data: images, 
#                videos files, audio files, etc.
# ================================================================
#                        File Path
# ================================================================ 
# A file path defines the location of a file or folder in the O.S 
# There are two ways to specify a file path. 
# + 1. Absolute path: which always begins with the root folder. 
#      The absolute path inclides the complete directory list 
#      required to locate the file. 
#      For example: /user/username/folder/file.extension
# + 2. Relative path: which is relatiove to the program's current 
#      working directory. 

# ==========================================================
#                     Opening Files - open()
# ==========================================================      
# To open a file in Python, you can use the built-in open(). 
# It takes two arguments: 
# + 1. the file path 
# + 2. mode in which to open the file
# This function returns the file object, which is used to
# read or write the file according the access mode.
# ===================================================================
#                    Access mode - open()
# ===================================================================   
# Access mode represents the purpose of opening the file. 
# For example: 
# 'r'  -> it opens an existing file to read-only mode. 
# 'rb' -> it opens the file read-only in binary format. 
# 'r+' -> it opens the file read and write both. 
# 'rb+' -> it opens the file to read and write both in binary format 
# 'x' -> it opens the file to write only. It not overwrites the file 
#        if previously exist but raise an error if no file exist.
# 'w' -> it opens the file to write only. It overwrites the file 
#        if previously exist or creates a new on if no file exist 
#        with the same name. 
# 'wb' -> it opens the file to write only in binary format. 
#         It overwrites the file if it exits previously or creates 
#         a new one if no files exists.
# 'w+' -> it opens the file to write and read data. 
#         It will override existing data. 
# 'wb+' -> it opens the file to write and read both in binary format 
# 'a' -> it opens the file in the append mode. It will not override 
#        existing data. It creates a new file if no file exist 
#        with the same name. 
# 'ab' -> it opens a file in the to append mode in binary format. 
# 'a+' -> it opens a file to append and read both. 
# 'ab+' -> it opens a file to append and read both in binary format.

file_path = '13_file_handling\\1_theory\\example.txt'
file_mode = 'r' # read
file = open(file_path, file_mode)

print(file.read())
file.close()

""" 
# ================================================================
#  Reading Files - read() - read(size) - readline() - readlines()
# ================================================================      
# To read or write a file, we need to open that file. 
# For this purpose, Python provides a built-in function.

# Opening file in current directory
relative_path = '13_file_handling\\1_theory\\message.txt'
file = open(relative_path, 'r')

# reading the file content
content = file.read()

# displaying the file content
print(content)

# closing the file
file.close()

# ==========================================================
#                        Writing Files
# ==========================================================
# In order to write into a file in Python, 
# we need to open to open it in write mode by passing 'w' 
# inside open() function as a second argument

# Create a new file with open() function on write mode
second_path = '13_file_handling\\1_theory\\message_2.txt'
file2 = open(second_path, 'w')
phrase = 'Python is insane :v'
file2.write(phrase)

# ===============================================
#                  Writing - Reading

third_path = '13_file_handling\\1_theory\\message_3.txt'
file3 = open(third_path, 'r+')
phrase = 'Welcome\nHow are you?'
file3.write(phrase)
file3.seek(0)
print(file3.read())

"""
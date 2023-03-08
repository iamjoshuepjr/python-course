# Input/Output Python File Operation

# =========================================================================
#  A file is a container in computer storage devices used for storin data 
#  When we want to read from or write to a file, we need to open it first. 
#  When we aew done, it needs to be closed so that the resources that are 
#  tied with the file are freed. 
#  Hence, in Python, a file operation takes place in the following order:
#  1. Open a file 
#  2. Read or write (perform operation) 
#  3. Close the file

# ===================================================
#               Creating and Opening Files in Python
# In Python, we use the open() method to open files
 
# Opening file in current directory
relative_path = '9_file_handling\\message.txt'
file = open(relative_path, 'r')

# reading the file content
content = file.readline()

# displaying the file content
print(content)

# closing the file
file.close()

# ==========================================================
#                             Writing Files
# In order to write into a file in Python, 
# we need to open to open it in write mode by passing 'w' 
# inside open() function as a second argument

# Create a new file with open() function on write mode
second_path = '9_file_handling\\.txt'
file = open()



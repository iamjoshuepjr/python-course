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
#               Opening Files in Python
# In Python, we use the open() method to open files

# Opening file in current directory
file = open('test.txt', 'r')

# reading the file content
content = file.read()

# displaying the file content
print(content)

# closing the file
file.close()
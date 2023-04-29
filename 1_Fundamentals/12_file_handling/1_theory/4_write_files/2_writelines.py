""" 
 =====================================================================
        writelines()
 =====================================================================
 We can write a multiple lines at once using the writelines().
 We can pass a list of strings that we want to add to the file to it.
 Use this method when you wanted to write a list into a file.
"""

person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
# writing string and list of lines to a file
fp = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\8_write.txt', 'w')
fp.writelines(person_data)
fp.close()

# =============================
# opening the file in read mode
# =============================
fp = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\8_write.txt', 'r')
print(fp.read())
fp.close()

# =================
#  with statement
# =================
name = "Written using a context manager"
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\9_write.txt', 'w') as f:
    f.write(name)

# ==================================================
#  Opening the file in read mode to access the file
# ==================================================
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\9_write.txt', 'r') as f:
    print(f.read())

# =============================================
#  Appending new content to an existing file
# =============================================
name = '\nName: Ava'
address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
# append to file
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\8_write.txt', 'a') as f:
    f.write(name)
    f.writelines(address)

# opening the file in read mode to access the file
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\8_write.txt', 'a+') as f:
    print(f.read())

name = '\nName: Antony'
address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
# append to file
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\8_write.txt', 'a+') as f:
    f.write(name)
    f.writelines(address)
    # move file handle to the start
    f.seek(0)
    print(f.read())
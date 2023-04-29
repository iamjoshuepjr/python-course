"""
 ===============================================================
                 Write file 
 =============================================================== 
 We can open a file and do different operation on it, such as 
 write new content into it or modify a file by appending content 
 at the end of a file. 
 ===============================================================
   File mode                Meaning 
 =============================================================== 
 w            Open a file for writing. In the case if an 
              existing file, it truncantes the existing content 
              and places the filhandle at the beginning of the file.
              A new file is created if the mentioned file doesn't exist. 
              
 w+           Open a file for both reading and writing. 
              In the case of the exiting file, it will truncate 
              the entire content and place the filehandle at the
              beginning of the file.
 
 wb           Open a binary file for writing. The filehadle is placed 
              at the beginning of the file, and existing content 
              will be truncated. A new file is created otherwise.              

 a            Opens file for writing. The filehadle is placed 
              at the end of the file. In the case of existing file, the 
              new content will be added after the existing content. 
              A new file is created otherwise.              

 a+           Opens file for appending as well as reading. 
              The filehadle is placed at the end of the file. 
              In the case of existing file, the new content will 
              get added after the existing content. 
              A new file is created otherwise.              
"""
text = "This is to be written"
file = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\7_write.txt', 'w')
file.write(text)
print('Done writing')
file.close()

file = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\7_write.txt', 'r')
print(file.read())
file.close()

text = "This is new content to be written"
file = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\7_write.txt', 'w+')
file.write(text)
print('Done writing')
file.close()

file = open('1_Fundamentals\\12_file_handling\\1_theory\\files\\2_write\\7_write.txt', 'r')
print(file.read())
file.close()
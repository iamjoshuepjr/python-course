""" 
 =========================================================
        readline() Read a file line by line
 =========================================================
 By default, this method reads the first line of the line. 
 You can use a loop to read the first five lines using the 
 readline() method in the loop's body.
"""
print('\n+--------------------------------\
     \n- Reading the file line by line -\
     \n+--------------------------------\n')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  line = file.readline()
  print(line)
  line = file.readline()
  print(line)
  line = file.readline()
  print(line)
  line = file.readline()
  print(line)

print('\n+-----------------------------------------\
     \n- Reading first N lines using readline() -\
     \n+-----------------------------------------\n')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  for i in range(4):
    print(file.readline().strip())

print('\n+---------------------------------------------\
     \n- Reading first and last line using readline() -\
     \n+-----------------------------------------------\n')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  first_line = file.readline()
  print(first_line)
  
  for last_line in file:
    pass 
  print(last_line)

print('\n+---------------------------------------\
     \n- Reading entire file using readline() -\
     \n+---------------------------------------\n')
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  line = file.readline()
  while line != '':
    print(line, end='')
    line = file.readline()
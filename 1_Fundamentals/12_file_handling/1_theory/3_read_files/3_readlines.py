""" 
 =========================================================
        readlines()
 =========================================================
 This method will returns the entire file contents. 
 The reading of the content will start from the beginning 
 of the file till it reaches the end of the file. 
 This method will internally call the readline() method and 
 store the contents in a list. 
 The output of this method is a list.
"""
print('\n+-------------------------------\
     \n- Reading file using readlines() -\
     \n+---------------------------------\n')

with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  lines = file.readlines()
  print(lines)

print('\n+----------------------------------\
     \n- Reading firts n lines from a file -\
     \n+------------------------------------\n')
N = 3
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  head = [next(file) for x in range(N)]
  print(head)

print('\n+-----------------------------------\
     \n- Reading the last n lines in a file -\
     \n+-------------------------------------\n')

N = 3
with open('1_Fundamentals\\12_file_handling\\1_theory\\files\\1_empty\\1_empty.txt', 'r') as file:
  lines = file.readlines()[N:]
  print(lines)
'''
for iterating_var1 in sequence:  #outer loop
    for iterating_var2 in sequence:  #inner loop

'''

rows = int(input("Enter the rows:"))
for i in range(1,rows+1):
    for j in range(i):
        print(i,end = '')
    print()

# User input for number of rows
rows = int(input("Enter the rows:"))
# Outer loop will print number of rows
for i in range(1,rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*",end = '')
    print()


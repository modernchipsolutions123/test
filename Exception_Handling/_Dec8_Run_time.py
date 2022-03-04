
#Run_time Error: At run-time while executing the program something goes wrong
#ZeroDivisionError: division by zero
x = int(input("Enter the 1st nbr : "))  #10
y = int(input("Enter the 2nd nbr: "))   #0
print(x/y)

##ValueError: invalid literal for int() with base 10: "''"
x = int(input("Enter the 1st nbr : "))  #10
y = int(input("Enter the 2nd nbr: "))   #'5'
print(x/y)

#FileNotFoundError: [Errno 2] No such file or directory: 'xyzxyz.txt'
f= open('xyzxyz.txt')
print(f.read())



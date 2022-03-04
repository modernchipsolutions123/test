#Reading characters from file
#Open the file for reading data
f = open("myfile.txt",'r')
#Read all characters from file
str = f.read()
#display them on screen
print(str)
f.close()


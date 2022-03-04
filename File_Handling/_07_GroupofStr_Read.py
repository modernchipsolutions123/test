#Create file with string and read the data from the file
f = open("myfile.txt",'r')
#Enter strings from keyword
print('The file contents are : ')
#Read strings from the file
str = f.read()
print(str)
f.close()

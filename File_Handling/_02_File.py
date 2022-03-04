obj2 = open("E:/file/file2.txt","w")
obj2.write("This is Sai ganesh")
obj2.close()

#append a ,It used to add some more data to the file
obj2 = open("E:/file/file2.txt","a")
#write() : It is used to write data to the file
obj2.write("I am from BHIMAVARAM")
obj2.close()

obj2 = open("E:/file/file2.txt","r")
#Read(): read th output from the file
s1 = obj2.read()
print(s1)
obj2.close()
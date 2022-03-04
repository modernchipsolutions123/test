'''
#File_Handling:Your program output is used to store permanant in external and hard disk or
    a read input from the file .THere are four methods
1.open() : It can allow only two parameters -->open(name,mode)
2.close() :Close the file.When we open the file after complete to add data.we have to close file
3.write() :TO write data into file.If any data is already present in th file,it would be deleted and present data stored
4.read() :To read data from the file.The file pointer is pointed at the begining of the file

'''
#1.Create the file by using obj of that file and open
obj1 = open("E:/file/file1.txt","w")
#2.It is used to add data or content to the file by using write()
obj1.write("Hello Dhana this is Sai") #It is used to stor data permanently
#it is to closed the file bt using close.Without close the file we can't add data to the file
#print(obj1)
obj1.close()
#Read data from the file
obj1 = open("E:/file/file1.txt","r")
s = obj1.read()
print(s)
obj1.close()

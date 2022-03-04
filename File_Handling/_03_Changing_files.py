'''
By changing file or Delete file
By changing folder or delete folder
Create seperate folder and add all files
checking directory
#We have diff methods by using this method and How to store permanently data by using
OS class
import os module
'''
import os
#1.Changing file name file2 to sai1.txt
# os.rename("E:/file/file2.txt","E:/file/sai1.txt")
#2.Delete the file by using remove method
#os.remove("E:/file/sai1.txt")
#print("file remove")
#3.Create new Folder INDIA
#os.mkdir("E:/INDIA.txt")
#4.Change dirextory
#os.chdir("E:/INDIA.txt")
#print("Get current working directory:",os.getcwd())
os.rmdir("E:/INDIA.txt")
'''f_open = open("dhana.txt","w")
f_open.write("This is sai ganesh")
f_open.write(" This is sai ")

f_open.close()

f_open = open("dhana.txt","w")
f_open.write("This is gani")
f_open.write(" This is dhana ")
f_open.close()

f_open = open("dhana.txt","a")
f_open.write("This is python ")
f_open.write(" Welcome to my world")
f_open.close()'''
#open the file for writing
f = open('myfile.txt','w')
#Enter characters from keyword
str1 = input("Enter text: ")
#Write string into file
f.write(str1)
#Close the file
f.close()




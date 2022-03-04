f = open("myfile.txt",'w')
#Enter strings from keyboard and print
print('Enter text (@ at end): ')
#It will execute upto the string is not equal to @
while str!='@':
    str = input()   #Accept string into str
    #Write the string into file
    if(str != '@'):
        f.write(str + "\n")
f.close()



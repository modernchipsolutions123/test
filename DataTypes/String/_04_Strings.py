'''
STRING : It is used i singlr quotes,double quotes,tripple quotes
    str1 = "Sai"
    str2 = 'gani'
    Example : One string write in different ways
    str3 = "Kadali's note book"
    str3 = 'Kadali\'s  note book'

'''
str = "Python for beginners"
print(str)
print("Length of the string :",len(str))
#INDEX : Index start with zero and ends with len(str)-1 and space also index
print("By using 1st indexes : ", str[0])
print("By using indexes 'Sapce': ", str[6])
#By using -ve we print in a reverse order
print("Negative index :", str[-1])
print("Negative  index space :", str[-10])
print("Length of string :", len(str))
print("It will print all in Uppercase:",str.upper())
print("It will print  T/F :", str.isupper())
print("it will all strings in lower case :",str.lower())
print("It is lower/not T/f :", str.islower())
print("It will print starting of every first letter is capital",str.title())
print("It will print first letter is capital :",str.capitalize())
print("It will count the no of strings in given count :",str.count("o"))
print("It fill find the index of starting index :",str.find("for"))
print("It fill find the index of starting index :",str.find("r"))
print("It fill find the index of starting index :",str.replace("for","is a"))
print("It fill find the index of starting index :","*".join(str))
'''s1 = "Welcome"
s = s1.center(10,"s")
print(s)'''




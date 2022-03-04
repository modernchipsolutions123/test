"""
STRING : String is a sequence of character eith e with single quotes/double quotes
        In python most commonly used this string data type because by default everything is string
        Python will give most important to python
    1.In python string is used in single quotes('')/double quotes("")/triple quotes(''')
    2.Triple quotes is used to multi line  string literials statement
     ex: str = 'sai'
        str1 = "kadali"
        str2 = '''ganesh
                        is
                        a
                        bad boy'''

"""
#Escape character by using single quotes
s = 'Ballu come\'s quickly ' #by using backslash we use  this statement
s1 = "Ballu come's quickly"
s2 = '''Ballu come's quickly'''

str1 = "Kadali"
print("Length of the string :", len(str1))
#1.Index values: Index value start from 0 to len(str)-1 and by using reverse order -1 to len()
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
#print(str1[9]) String index out of range
#2.Slicling : slicing is used to [start:end:stop]
str2 = "Sravani"
print("Length of the string2:",len(str2))
print(str2[0:])
print(str2[1:])
print(str2[1:4])
print(str2[1::2])
print(str2[::2])
print(str2[-1::]) #It will print reverse value
print(str2[::-1]) #It will print in a reverse order
print(str2[::1])
#3.Count : count is used to print all the occurences in string
str3 = 'kadali'
print(str3.count('a'))
#3.find() : Find method is used to provide the index of first occuerence


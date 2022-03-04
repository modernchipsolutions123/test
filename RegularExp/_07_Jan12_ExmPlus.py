#+  ---> One or more occurences
import re
str = "Welcome to the meta in dot characters in regular expressions"
str2 = "Ineed a firendd and i need a chicken"
res = re.findall("t+",str)
print(res)
res = re.findall("e+",str2) #. --> One or more
print(res)
res = re.findall("d+",str)
print(res)
#{} ---> Specified no.of occurences
res = re.findall("e{1}",str)
print(res)
res = re.findall("e{2}",str2)
print(res)
res = re.findall("d{2}",str2)
print(res)





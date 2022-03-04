#*  ---> Zero or more occurences
import re
str = "Welcome to the meta in dot characters in regular expressions"
str2 = "Ineed a firend and i need a chicken"
res = re.findall("t*",str)
print(res)
res = re.findall("m*",str)
print(res)
res = re.findall("char*",str)
print(res)
res = re.findall("ee*",str2) #Zero or more occurences
print(res)
#+  ---> One or more occurences
print(res)
res = re.findall("ee+",str2) #one or more occurences
print(res)
print(res)
res = re.findall("in*",str2)
print(res)
#findall()	It returns a list that contains all the matches of a pattern in the string.
# .  ---> Any character except new line
import re
str = "Welcome to the meta in dot characters in regular expressions"
res = re.findall("Wel....",str)
print(res)
res = re.findall("Wel....",str)
print(res)
res = re.findall("Wel.",str)
print(res)
res = re.findall("Wel......",str) #Space is also a character
print(res)
res = re.findall("...Welc",str) #Return empty list there was no start with any other
print(res)
res = re.findall("..r",str)
print(res)






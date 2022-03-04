#Pattern Matching:  Meta Characters - Special Sequences - Sets
'''
META CHARACTERS :
[] --> return a match if the string contains pattern/characters specified in []
^  ---> retuen a match if string starts with given pattern
$  ---> End with particular word
.  ---> Any character except new line
*  ---> Zero or more occurences
+  ---> One or more occurences
{} ---> Specified no.of occurences
findall()	It returns a list that contains all the matches of a pattern in the string.

'''
import re
str = "Welome to the meta characters in regular expressions"
#Using []
res = re.findall("[e]",str)
print(res)
res = re.findall("[th]",str) #It will take a characters not string
print(res)
#Using ^  ---> retuen a match if string starts with given pattern
res = re.findall("^Welome",str)
print(res) #It will return in list with starting of string
res = re.findall("^regular",str)
print(res) #Match fails only starting string
#Using $
res = re.findall("expressions$",str)
print(res) #It will return Match end with given string
res = re.findall("regular$",str)
print(res) #Match fails when given string is not ending









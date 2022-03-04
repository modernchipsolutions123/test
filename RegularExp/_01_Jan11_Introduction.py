'''
REGULAR EXPRESSION: Sequence of character used for pattern matching
    pattern ---> Character or group of char
1.The module re provides the support to use regex in the python program.
2.The re module throws an exception if there is some error while using the regular expression.

In-Built methods:
1.match()	This method matches the regex pattern in the string with the optional flag. It returns true if a match is found in the string otherwise it returns false.
2.search()	This method returns the match object if there is a match found in the string.
3.findall()	It returns a list that contains all the matches of a pattern in the string.
4.split()	 Returns a list in which the string has been split in each match.
5.sub() 	Replace one or many matches in the string.
'''
#findall():
import re
str = "How are you. How is everything"
matches = re.findall("are", str)
print(matches)
#If it is not found it will give empty list
matches = re.findall("Sai", str)
print(matches)
#Iterating
matches = re.finditer("How", str)
#print(matches)
for each in matches:
    print(each)
#search()
matches = re.search("How", str)
print(type(matches))
print(matches)  # matches is the search object
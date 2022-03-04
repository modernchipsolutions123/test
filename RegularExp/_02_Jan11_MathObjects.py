'''
#Match object methods :
1.span(): It returns the tuple containing the starting and end position of the match.
2.string: It returns a string passed into the function.It has no callable object -->()
3.group(): The part of the string is returned where the match is found.

'''

import re
str = "Haii i am new to python programming"
matches = re.search("Haii",str) #If it is find thenIt will give name of object and index of string
print(matches)
print(matches.start()) #It will give index value of given string of first occurence

#matches = re.search("xyz",str)
#print(matches) #If it is not found thenIt will give None
#returns tuple containing starting and end position of string in match
print(matches.span())
#returns a string passed into the function.
print(matches.string) #String has no callable object
#The part of the string is returned where the match is found
print(matches.group())
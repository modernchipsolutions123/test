import re
str = "I am Sai from Bhimavaram"
# re.split("pattern",source_string,optional(maxsplit))
x = re.split("a",str)
print(x)
y = re.split("M",str)
print(y)
#sub-->It is used to replace with another pattern split method
#re.sub("pattern",source_string,optional(no.of ocurrences))
x = re.sub("a","A",str) #It will replace with another pattern split method
print(x)

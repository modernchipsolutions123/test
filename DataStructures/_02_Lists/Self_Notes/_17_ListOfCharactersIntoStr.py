#21.List of characters into string
List_char = ['s', 'a', 'i', 'g', 'a', 'n', 'e', 's', 'h', 'k', 'a', 'd', 'a', 'l', 'i']
str1 = ''.join(List_char)
print(str1)
c1 = ['k', 'a', 'd', 'l', 'i', 'r', 'a', 'm', 'y', 'a' ]
str2 = ''.join(c1)
print(str2)
#By using function
s = ['k', 'd', 'a', 'l', 'i', 's', 'r', 'a', 'v', 'a', 'n', 'i']
def convert(s):
    # initialization of string to ""
    new = ""
    # traverse in the string
    for x in s:
        new += x
        # return string
    return new
print(convert(s))



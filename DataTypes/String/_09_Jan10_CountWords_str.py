'''str1 = input("Enter the String : ")
char = 0
wrd = 1
for i in str1:
    char = char + 1
    if i == ' ':
        wrd = wrd + 1
print("No.of Characters appear in string: ",char)
print("No.of Words appear in string: ",wrd)'''
# initializing string
test_string = "Kadali sai ganesh"
# printing original string
print("The original string is : " + test_string)
# using split()
# to count words in string
res = test_string.count('a')
# printing result
print("The number of words in string are : " + str(res))
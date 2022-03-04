#Swapping last char of string
'''str1 = input("Enter the string :" )
#print("It will print last character of string: ",str1[-1:])
#print("It will print first character of string: ",str1[:1])
#print(str1[1:-1])
print(str1[-1:] +  str1[1:-1] + str1[:1])'''
str2 = input("Enter the String: ")
def lastChar_Swap(str2):
    return str2[-1:] + str2[1:-1] + str2[:1]
print(lastChar_Swap(str2))




#String is an single or double quotes('',"") and it is an data type
#1.Length of the String by using In-Built methods
s = "Welcome to python"
print("Length of the string: ",len(s))
#2.Count characters in string
print("Count character of given string:",s.count('o'))
#3.String slicing[start:end:step]
print("String slicing by using starting index:",s[0:])
print("String slicing by using negative index at starting poit:",s[-1:])
print("String slicing by using negative index at ending point(Reverse order):",s[::-1])

#4.String replace
s1 = "Welcome to python program,in Bangalore"
s1 = s1.replace('o','e')
print("Replace o with e in given string :",s1)

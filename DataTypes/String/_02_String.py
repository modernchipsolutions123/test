
'''
#find() : This method is used to return the index of first occurence
s =  'abcabcabca'
index 0123456789
s.find('abc')

#find('abc',beganindex,endindex-1)
It will search 3rd index to 9th index
s.find('abc',3,10 or len(s))
'''
'''
s = 'abcabcabca'
print("Index of first occurence is :",s.find('abc'))
print("Length of string :",len(s))
print("It will substring find 3rd index to 9th index:",s.find('abc',3,10))
print("It will  substring find 6th index to 9th index: ",s.find('abc',6,10))
print("It will  substring find 9th index to 9th index: ",s.find('abc',9,10))

#How to find index of all occurences
s ='abcabcabc'
subs = 'abc'
i = s.find(subs)
if i == -1:
    print('Substring is not found')

while (i! ==-1):

course = "Python for begineers"
another = course[:]
#print(another)

name = "jennifer"
print(name[1:-1])
'''
#Print john [smith] is a coder
first_name = "John"
last = "Smith"
print("First way to print :",first_name + ' [' + last + ']' + " is a coder" )
last1 = "[smith]"
print("Second way to print :",first_name + last1 + "is a coder")
last2 = "smith"
#Concatination
message = first_name + ' [' + last2 + ']' + " is a coder"
print("Third way to print :",message)
#String formatting
msg = f'{first_name} [{last}] is a coder'
print(msg)



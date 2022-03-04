'''#1.Length of the string by using for loop
s1 = "This is Sai ganesh kadali"
for i in s1:
    print(i)
print("Length is 0 to n-1:",len(s1))
#2.Count character of a string by using for loop
s1 = input("Enter the string name: ")
for i in range(len(s1)):
    print("Count characters of a string:",i,s1[i])

#3.String slicing by using for loop
msg = "Helloworld"
print("Given string:",msg)
for i in range(len(msg)): #length of msg is 0 to n-1
    print("1.String slicing by using for loop [start:stop:next]:",msg[0:])
    print("2.String slicing by using for loop in reverse:", msg[::-1])
    print("3.String slicing by using for loop in reverse 2 steps:", msg[0::2])
    print("4.String slicing by using for loop in reverse 2 steps:", msg[0::1])

#start: i = 0 -> stop: i +1 = 1 [0 : 1]
#start: i = 1 -> stop: 1 + 1 = 2 [1 : 2]'''
name = "Sai1223"
name.i

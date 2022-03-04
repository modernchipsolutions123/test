'''
1. In this python every object have an different address in alphabetical order
2.
st = 10
l = 5
tp =3
sets =2
'''

s = "Sai"
s1 = "Ganesh"
print(id(s))
print(id(s1))
print("............")
print("It will print diff addss S",id(s[0]))
print("It will print diff addss G",id(s1[0]))
print("..........")
print("It will print same address a",id(s[1]))
print("It will print same address a",id(s1[1]))
print(".......................")
print("i =", id(s[2]))
print("n =",id(s1[2]))
#In-Bult method for len(str)
print("Length of string: ",len(s1))
for i in s1:
    print(i)
    print(len(s1))

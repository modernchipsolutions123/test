from itertools import permutations
str1 = '()'
n = int(input("Enter the number: "))
str2 = str1*n

li1 = [i for i in str2]

li2 = permutations(li1)
li3 = []
for i in li2:
    a = "".join(i)
    li3.append(a)

li4 = []
for i in li3:
    if i in li4:
        pass
    else:
        li4.append(i)
li5 = []
for value in (li4):
    if value.startswith(')') or value.endswith('('):
        pass
    else:
        li5.append(value)

print(li5)
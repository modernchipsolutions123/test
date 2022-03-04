list = [1,2,3,4,5,6]
#Slice is [start:next:stop]
print(list[0])
print(list[1])
print(list[2])
print(list[::2])
String = 'Welcome to python'
s1 = slice(3)
s2 = slice(1, 5, 2)
print("String slicing")
print(String[s1])
print(String[s2])

#List slicing
L = [1, 2, 3, 4, 5]
s1 = slice(-3)
s2 = slice(-1, -5, -2)
print("\nList slicing")
print("It will print in reverse: ",L[s1])
print(L[s2])

# Tuple slicing
T = (1, 2, 3, 4, 5)
s1 = slice(-3)
s2 = slice(-1, -5, -2)
print("\nTuple slicing in reverse ")
print(T[s1])
print(T[s2])

class Slice_exm:
    def slice_mtd(self):
        String = 'Welcome to python'
        print(String[::-1])
sl1 = Slice_exm()
sl1.slice_mtd()



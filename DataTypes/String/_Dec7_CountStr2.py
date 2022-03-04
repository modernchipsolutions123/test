#Count characters in String
#In-built
str1 = "Welcome to python program"
print(str1.count('o'))

#By using for loop
'''
1.Take a string
2.
'''
n = input("Enter the String: ")
d1 = dict()
for c in n:
    #print(c)
    if c in d1:
        d1[c]+=1
    else:
        d1[c]=1
print(d1)

#3.By using oops and loops:
class Str2_De6:

    def Str_Count(self):
        n = input("Enter the String: ")
        d1 = dict()
        for c in n:
            # print(c)
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        print(d1)
c1 =  Str2_De6()
c1.Str_Count()
#4.By using oops:
'''class st_count:
    def str_Cou(self):
        str1 = "Kadali Durga malleswari"
        print("Count Character of a string :",str1.count('a'))
st1 = st_count()
st1.str_Count()'''



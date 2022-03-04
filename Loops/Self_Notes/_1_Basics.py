#For -->
for i in range(1,10):
    print("Using for loop:",i)
    #print(10)

l1 = [1,2,3,4,4]
for i in l1:
    print("It will iterate the list l1:",l1)
    print("It will iterate one by one in l1 to i: ", i)


n = int(input("Enter the number: "))
for i in range(11):
    c = n * i
    print(n,"*",i,"=",c)

sum = 0
n = input("Enter the number :")
for i in range(10):
    sum+=1
print("The sum is: ", sum)


n = int(input("Enter the value of n : "))
for j in range(11):
    c = n * j
    print(n,"*",j,"=", c )



#1.String
str = "Python"
for i in str:
    print(i)    #It  can iterate line by line  str to i
    print(str)  #It will print string line by line


#2.List
l1 = [1,2,3,4,"sei",3.4]
for i in l1:
    print("List",i)
    print(l1)
#3.Tuple:
l2 = ("sai","gani","dhana","sudharsh")
for i in l2:
    print("Tuple:",i)
#4.Dictionary
dic1 = {"Sai": 1,"gani": 2,"dhana":3}
for i in dic1:
    print("Dic:",i)





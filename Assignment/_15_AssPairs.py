#1.Ask user for input integers
#2.Convert to list
#3.Given user output lis
#4.Given input inegers as list in pairs
#5.print in a list

'''
#list1 = []
while(True):
    try:
        nbr = input("Enter the number : ")
        if(nbr =='exit'):
            break
        else:
            list1.append(int(nbr))
    except:
        print("Enter numbers only.")

print(list1)

list1 = []
n1 = eval(input("Enter the number: "))
#for i in range(n):
    #nbr = input("Enter the nbr:")
    #list1.append(int(nbr))
    #nbr = int(input("Enter the nbr:"))
    #list1.append(nbr)
    print("Enter the list: ",list1)
set1 = {}
s = list1(set1)
print(s)
print(n1)
list1.append(n1)
print(list1)
'''
#list1=[]

#1.Ask user for input integers
#2.Convert to list
#3.Given user output list
#4.Given input inegers as list in pairs
#5.print in a list then the out put is 7
class A:
    def sum_is(self):
        #1.Tke input from the user
        num = int(input("Enter the value : "))
        list1 = []#create an empty list to add an elements to list
        for i in range(num):
               # print("1.Value of i :",i)
            for j in range(num):
                #print("2.Value of j :",j)
               # print("i =",i,"j =",j)
                if j <= num//2:
                    if i+j == 7:
                        print(i,j)
                        list1.append((i, j))

        print(list1)
a = A()
a.sum_is()








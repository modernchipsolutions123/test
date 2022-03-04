#3.Largest nbr from list
l1 = [1,40,99,50,55]
print("Largest nbr by using in-built method:",max(l1))
#Create empty list
l1 = []
#No.of elements enter into the list
num = int(input("Enter the number of elements in list:"))
# iterating till num to append elements in list
for i in range(1,num+1):
     ele = int(input("Enter elements: "))
     l1.append(ele)
# print maximum element
print("Largest element is:", max(l1))





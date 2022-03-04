'''l1 = [1,2,1,3,4,5,3]
#l2 = [6,7,1,2,9]
#print("Concatinate :",l1 + l2)
print("Repeating", l1*2)
print(l1.count(3))
l1.remove(3) #It will remove the value
print("remove  value ::",l1)
print(l1)
l1.pop(0) #It will remove index value
print("pop  Index:",l1)
l1.clear()
print("It will clear all the elements in list :",l1)'''
l1 = [1,2,3,4,5,1,'sai']
l1.append(1)
print("By using append it will  add in last :",l1)
l1.extend(["Sai","gani","Kadali",1.2,9])
print(l1)
print("It will8"
      "8"
      "8count the no.of ",l1.count(1))
l2=l1.copy()
print("Copy list (l1) to l2:",l2)
print("It will print index value :",l1.index(3))
print("It will print index value :",l1.index('sai'))
print("It will remove the index element :",l1.pop(1))
print(l1)
l1.remove(1)
print("Remove the given element :",l1)
l1.reverse()
print("Reverse of a list :",l1)
#l1.sort()
#print("Sorting in list :",l1.sort())
#print()
#List by using oops:
'''class lis_exm:
      def __init__(self):
            pass

      def lis_mtd(self):
            l1 = [1,5,10,15,20]
            l2 = [2,4,6,8]
            print(sum(l1))
      # print(l1 + l2)
li1 = lis_exm()
li1.lis_mtd()'''
class list_exm:
      def __init__(self):
            pass
      def display(self):
            l1 =[1,2,3,4,5,6,7]
            l2 = [20,30,4.5]
            print("Sum of the elements in list:",sum(l1))
            print(l1+l2)

l1 = list_exm()
l1.display()
















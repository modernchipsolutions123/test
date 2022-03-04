'''
List properties:
==================
# 1. List will allow both homogeneous and heterogenous
# 2. List allows duplicate elements
# 3. Insertion order maintains
# 4. List is mutable
# 5. Follows indexing mechanism while storing elements
'''

# 1.List will allow both homogeneous and heterogenous
#Homogeneous : Same Data type
l1 = [1,2,3,4,5]
print("1.Integer in list",l1)
l1 = [1.2,23.4,2.0,1.66]
print("2.float in list",l1)
l1 = [True,False,True,False]
print("3.Boolean is list", l1)
l1 = ["Sai","gani","Kadali"]
print("String is list:",l1)
#Same data structures
l1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Lists is LIst:",l1)
l1 = [(1,1,2.3,3.4),(5.5,6.9),(8.9,9.0)]
print("Tuple is list",l1)
l1 = [{"Sai":1,"gani":2,"Kadali":3},{1:1,2:2.4}]
print("Dictionary is list:",l1)
l1 = [{1,2,3},{4,5,6},{7,8,9}]
print("Set is list:",l1)

#Heterogeneous
l1 = [1,2.4,"Sai",True,False,[1,2,3],(4,5,6),{1:10,2:20},{1,2,3}]
print("Heterogeneous:", l1)

#2.List can allow duplicate values
l1 = [1,1,2,2,3]
print("List can allow duplicate values:",l1)
#3.List is mutable
l1 = [1,2,3,4,5]
print("Before changing list l1:",l1)
l1[0] = 10
print("After changing list l1:",l1)
#4.List fallows index values machanism
l1 = [1,2,3,4]
#Index:0 1 2 3
print("List fallows index values:",l1)
#5.List fallows insertion order
l1 = [20,40,30,80,90]
print("list maintains Insertion order is :",l1)


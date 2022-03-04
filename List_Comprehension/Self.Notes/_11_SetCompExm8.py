myset1 = {1,2,3,4,5,6,7,8,9}
print("Origional set is : ",myset1)
s1 = [{ele for ele in myset1 if ele % 2 == 0}]
print("Print only reminder 0 ele: ",s1)
#Change datatype from set
s2 = [{str(ele1) for ele1 in myset1 }]
print("Converting integer to string: ",s2)
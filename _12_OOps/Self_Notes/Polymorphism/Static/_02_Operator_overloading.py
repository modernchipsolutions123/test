class Operator_overloading():
    a = 20
    b = 30
    list1 = [1,2,3]
    list2 = [1,2,3]
    list3 = [4,5,6,7]
    name1 = 'kadali'
    name2 = "sai"

obj1 = Operator_overloading()
print("1.Adding two operators with one operend(+) :", obj1.a + obj1.b)
print("2.Adding two lists :", obj1.list1 + obj1.list2)
print("....................................")
print("3.Using == Operator used to compare ele :", obj1.list1 == obj1.list2)
print("4.Is Operater used to compare Address :", obj1.list1 is obj1.list2)
print("......................................")
print("5.Adding all the Elements of List1,2,3 :", obj1.list1 + obj1.list2 + obj1.list3)
print("6.Sum of a,b is :", obj1.a + obj1.b)
print('................................')
print('7.Adding names :', obj1.name1 + obj1.name2)

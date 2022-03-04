dic1 = {"name":"Kadali","id" : 100,"salary":40000,"village":"Mulalanka"}
dic1= dic1.fromkeys(["Shiva","Nagarjuna","ragavendra"],10)
print("Dictionary from Fromkeys: ",dic1)
#Retrive all keys from dictionary
print(".......KEYS........")
d1 = dic1.keys()
print(d1,type(d1))
d1 = list(dic1.keys())
print("This keys will print in list : ",d1)
#By using for loop in dictionary
for key in dic1.items():
    print(key)

print(".......Values.......")
d2 = dic1.values()
print(d2)
d2 = list(dic1.values())
print(d2)
for value in dic1.values():
    print("It will print only values: ",value)
print("......Items........")

items= dic1.items()
print("It will print all the items of dic1 :",items)
items = list(dic1.items())
print("It will print all the items in a List: ",items)

n1, n2 = (150, 12.5)  # tuple unpacking
print(n1,n2)
for item in dic1.items():
    print(item)

print("......key,value......")
for key,value in dic1.items():
    print(key,value)

# By using List: 4. update()
print("-----------4. update() ----------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 4. update() : It will update key,values from dic2 to dic1
print("-----------4. update() ----------")
dic3 = {1:"sai", 2:"Gani", 3:"Kadali"}
dic4 = {"4:""Ramya", "5:""Sravani", "6:""Rajesh"}
dic3.update(dic4)
print(dic3,dic4)
print(".........Dictionary........")
dic1 = {1:"Sai",2:"Gani"}
#FromKey : Fromkey is used to pass sa
dic1 = dic1.fromkeys([11, 12, 20, 10], "Kadali")
print("Dictionary from keys : ", dic1)
dic1 = dic1.fromkeys([1,2,3,4],"Sai Ganesh")
print(dic1)

#dict1 = {1: 1, 2: 2, 'Hello': 'Dinesh'}
#print("Has key : ", dict1.has_key('Hello'))

dic1 = {1:"k",2:'S',3:'G'}

for i,j in dic1.items():
   # print("Key:",i)
   # print("Value:",j)
    print("Key:",i,"Value",j)



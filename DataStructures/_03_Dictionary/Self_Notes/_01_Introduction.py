#LOW-LEVEL In Dictionary :
'''

#Dictionary:I has key and value pairs and dictionary has empty set{key:value}.Unorder collections of data items
#In dictionary key must be unique and immutable(we can't change)
#In dictionary value can be anyone
dic1 = {'eid':1,
          'name':'Sai Ganesh',
          'sal':45000,
          'gender':'Male',
          'loc':'vizag',
          'pin': [123,246,367,478,365,469],
          'address':{'hno':'5-54/2','area':'MVP Colony'}
          }
print("it will print all the items in dic1",dic1.items())
print("It will print all the keys in dic1",dic1.keys())
print("It will print all the values in dic1",dic1.values())
print("House no :", dic1['address']['hno'])
print("Pin no   :", dic1['pin'][3])
print("gender:",dic1['gender'])
print("salary:",dic1['sal'])
'''
#Key must be Immutable value can be any thing
dict2 ={"100":10,200:{1,2,3.4},20.5:20,"Msg":["Kadali","Sai","ganesh",143],("Ramya","Sravani","Rajesh"):(1,2,3) }
print("Keys must be Immutable: ",dict2)
print("It will print all the key value pairs of dic2",dict2.items())
print("It will print all the keys i dic1: ",dict2.keys())
print("It will print all the values in dict2",dict2.values())

# [1,2,3] : {1:1,2:2},  # Wrong, List is mutable
         # {1:1,2:2} : "Hello"   # Wrong, dict is mutable
         # {1,2,3} : "Hello"     # Wrong, set is mutable'''





#Dictionary by using list
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
#Dictionary comprehension
mydic = {(k,v) for k,v in zip(keys,values) }
print(mydic)

#Dictionary by using list comprehension by using square
dic1 = {x:x**2 for x in [1,2,3,4,5,6]}
print(dic1)

#Dictionary by using string comprehension by using cube
dic2 = {y.upper():y*3 for y in "SaiGanesh"}
print(dic2)

dic3 = {a:a**2for a in range(1,11)}
print(dic3)

original_dic1 = {'sai':19,'gani':20,'kadali':100,'sravani':21,'ramya':22}
dic4 = {k:v for (k,v) in original_dic1.items() }
print("All the items in dictionary:",dic4)


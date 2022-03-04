#1.Print each item and its corresponding type from the following list
datalist = [123, 11.2, 1+2j, True, 'Python', (0, -1), [5, 12],{"Name":'Sai', "Village":'mlk'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
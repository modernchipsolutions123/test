Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
for x in Employee:
    #print("It will print only Keys",x)
    print("It will print only values ",Employee[x])
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
for x,y in Employee.items():
    print("X is Key: ", x ," Y is value: ",y)

for x in Employee.items():
    print(x)


#2.Add keys to dictionary
'''
1.Take dictionar empty{}
2.adding keys to dictionary one by one
3.print the dictionary
'''
dic1 = {} #Create empty dictionary
#Adding keys to dictionary
dic1["1"] = 'one'
dic1['2'] = 'two'
dic1['3'] = 'three'
print("Adding keys to dictionary",dic1)
dic1.update({'4':"four"})
print("After update the dictionary:",dic1)
print(dic1['2'])



#1.Create empty dictionary
dic1 = {}
# Assigning key and values into dictionary
dic1[2] = 'Twenty'
dic1['id'] = 200
dic1['name'] = "Kadali"
print("BY using empty Dictionary to update: ",dic1)


# UPDATE :By using keys we have to update the values
dic1[2] = 'Two'
dic1['id'] = 12
print("Update values By using keys:",dic1)
# UPDATE :By using keys we have to update the values
dic1['Twenty']  = 10
dic1[200] = 's'
dic1['kadali'] = 'g'
#We can't update keys by using values in dictionry
print("Update keys by using values:",dic1)


# RETRIEVE : It will print the values of a given key
print(dic1[2] )
print("Dictionary item: ",dic1['id'])
print("Dictionary item: ",dic1['name'])

# DELETE
print("Original dictionary:",dic1)
del dic1['id']
print("Delete the key of id:",dic1)
#del dic1[10]  KeyError we can't delete the value
#print("Delete the value:",dic1)
del dic1[200]
print("Delete the value by using key 200 :",dic1)
del dic1['Twenty']
print("Delete the value(10) by using key Twenty:",dic1)

print("Length of dict : ", len(dic1))

# str()
di_str = str(dic1)
print("Dict in string format :", type(di_str), di_str)

#1.Create empty dictionary
dic1 = {}
# Assigning key and values into dictionary
dic1[2] = 'Twenty'
dic1['id'] = 200
dic1['name'] = "Kadali"
print("BY using empty Dictionary to update: ",dic1)


# UPDATE :By using keys we have to update the values
dic1[2] = 'Two'
dic1['id'] = 12
print("Update values By using keys:",dic1)
# UPDATE :By using keys we have to update the values
dic1['Twenty']  = 10
dic1[200] = 's'
dic1['kadali'] = 'g'
#We can't update keys by using values in dictionry
print("Update keys by using values:",dic1)


# RETRIEVE : It will print the values of a given key
print(dic1[2] )
print("Dictionary item: ",dic1['id'])
print("Dictionary item: ",dic1['name'])

# DELETE
print("Original dictionary:",dic1)
del dic1['id']
print("Delete the key of id:",dic1)
#del dic1[10]  KeyError we can't delete the value
#print("Delete the value:",dic1)
del dic1[200]
print("Delete the value by using key 200 :",dic1)
del dic1['Twenty']
print("Delete the value(10) by using key Twenty:",dic1)

print("Length of dict : ", len(dic1))

# str()
di_str = str(dic1)
print("Dict in string format :", type(di_str), di_str)





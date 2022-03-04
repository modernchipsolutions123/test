dic1 = [{'Name':'Sai','age':26},
        {'Name':'Gani','age': 20},
        {'Name':'Dhana','age':25}]
names = []
for dic in dic1:
        if dic['age'] > 25:
                names.append(dic['Name'])
names = [dic['Name'] for dic in dic1 if dic['age'] > 24]
print(names)

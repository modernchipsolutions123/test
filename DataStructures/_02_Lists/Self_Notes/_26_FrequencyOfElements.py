#30.Frequency of Elements in list
l=[1,2,3,4,1,2,66,2,44,55,67,66,66]
print("Original list is :",l)
dict={}
for i in l:
    if i not in dict:
        dict[i]=1
    elif i in dict:
        dict[i]+=1

print("Frequency of Elements:",dict)



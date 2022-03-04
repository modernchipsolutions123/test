#29.Get Unique values from list
#Create a list
l2 = [111,222,33,44,222,33,55]
#Create an empty list
new_list = []
#pass the l2 elements to i
for i in l2:
#Repeated elements not allowed to i
    if i not in new_list:
        new_list.append(i) #Append the uniq elements into list
print("Unique elements in list:",new_list)

#By using function
def unique(list1):
    # initialize a empty list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x) #Append the unique elements in list
    # print list
    for x in unique_list:
        print (x)
# Create a list
list1 = [10, 20, 10, 30, 40, 40]
print("the unique values from 1st list is")
unique(list1)
list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)
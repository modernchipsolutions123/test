#32.Check a lists contain sublist
list1 = [1,2,3,4,5,6]
sub_list = [3,4,5,6]
count = 0
for i in sub_list:
    if i in list1:
        count +=1
        print(count)



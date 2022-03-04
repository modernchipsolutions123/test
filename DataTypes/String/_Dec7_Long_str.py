#Length of longest string in python
test_list = ['sai', 'ganesh', 'kadali', 'ganapathi']
print("The original list : " + str(test_list))

#LongestString in list
# using loop
class Long_str:
    def __init__(self):
        pass
    def lng_str(self):
        max_len = -1
        for ele in test_list:
            if len(ele) > max_len:
                max_len = len(ele)
                res = ele
        print("Maximum length string is : " + res)
l1 = Long_str()
l1.lng_str()
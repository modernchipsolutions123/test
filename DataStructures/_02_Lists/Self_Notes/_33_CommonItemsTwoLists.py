#37.Finding common items from two lists
a = [2,3,4,5,6,7,8]
b = [1,2,4,6,8,9]
a_set = set(a)
b_set = set(b)
if (a_set & b_set):
    print(a_set&b_set)
else:
    print("No common elements")
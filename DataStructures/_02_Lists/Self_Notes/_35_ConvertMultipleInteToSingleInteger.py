#39.Converting multiple integers into single integer
listA = [22,11,34]
# Given list
print("Given list A: ", listA)
# Use
res = int("".join(map(str, listA)))
# Result
print("The integer is : ",res)


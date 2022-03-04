from itertools import combinations
msg='saiganesh'.lower()

str2=[]
lst=[]
sub_strng=[]

for i in range(1,len(msg)+1):
    lst.append(list(combinations(msg, i)))
    # print(lst)
for i in lst:
    for item in i:
        sub_str=''.join(item)
        sub_strng.append(sub_str)
# print(sub_strng)
# print(sub_strng)
palindrome_stg=[]
for i in sub_strng:
    if i==i[::-1]:
        palindrome_stg.append(i)
print("Number of palindrome strings : ",len(set(palindrome_stg)))
print(set(palindrome_stg))
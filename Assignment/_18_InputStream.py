'''import itertools as it

large = -1
innum = int(input("Enter input number : "))
str_innum = str(innum)
combins = it.permutations(strinnum,len(strinnum))
for comb in combins:
    word = "".join(comb)
    if(word == word[::-1]):
        if(int(word) > large):
            large = int(word)

print(large)'''

import itertools as it
def grouper(innum):

    str_innum = str(innum)
    grouping = it.permutations(str_innum, len(str_innum))
    large = -1
    for combine_group in grouping:
        word = "".join(combine_group)
        if (word == word[::-1]):
            if (int(word) > large):
                large = int(word)

    return large
innum = int(input("Enter input number : "))

l = grouper(innum)
print(l)

def table(n):
    for i in range(1, 11):
        yield n * i
        i = i + 1
'''        print(i)
t1 = table(15)
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
'''
for i in table(15):
    print(i)
def tab(num):
    list1 = []
    for i in range(1,11):
        list1.append(f'{num} X {i} = {num * i}')
    return list1
t1 = tab(6)
for i in t1:
    print(i)

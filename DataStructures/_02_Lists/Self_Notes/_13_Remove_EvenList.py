#14. Remove Even elements and print List Items
evenList = [11, 22, 31, 44, 51, 55, 65, 71, 82, 91, 98]
print("List Items = ", evenList)
for ev in evenList:
    if (ev % 2 == 0):
        evenList.remove(ev)
print("List Items after removing even Items = ", evenList)

ev_l1 = [2,3,4,5,6,7,8,9,11,12,34,55,78,99]
print("List_items:",ev_l1)
for ev in ev_l1:
    if ev %2 ==0:
        ev_l1.remove(ev)
print("After removing even elements:",ev_l1)

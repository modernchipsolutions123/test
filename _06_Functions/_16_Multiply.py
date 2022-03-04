li1 = [2,4,-6]
def mul_list(li1):
    mul = 1
    for x in li1:
        mul *= x
    return mul
print(mul_list(li1))

t1 = (1,2,3,4)
def tp_mul(t1):
    mul1 = 1
    for i in t1:
        mul1 *=i
    return mul1
m1 = tp_mul(t1)
print(m1)


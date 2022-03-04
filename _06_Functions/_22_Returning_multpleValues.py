def sum_sub_mul_div(a,b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    #Returning multiple values
    return c,d,e,f
t = sum_sub_mul_div(20,30)
print("Results are:")
#Display results by using for loop
for i in t:
    print(i)
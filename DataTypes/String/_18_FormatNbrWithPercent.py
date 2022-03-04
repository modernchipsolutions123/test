#36.Format number with percentage
'''x = 0.25
y = -0.25
print("\nOriginal Number: ", x)
print("Formatted Number with percentage: "+"{:.2%}".format(x));
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.2%}".format(y));
print()'''

def format_perc(x,y):
    print("Original nbr :",x)
    print("original nbr y:",y)
    print("Format nbr with percentage:"+"{:.2%}".format(x))
    print("format nbr with percentage:"+"{:.2f}".format(y))
format_perc(10.0,20)


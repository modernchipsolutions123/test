"""
Functions : Function is used to code - reusability at multiple times
    1.Every function has a name with def keyword
    2.Every function has a name and should not match with anykeyword
    3.closed with paranthesis () and paraeter and arguments are optional ending with indentation
    4.Every function has a body
    5.Every function has calling itself by using name
    Syntax:
        def display():

            Body
        display()
"""

def display(): #1.Function deffination with name
    #State
    a = 10
    b=20
    c = a + b
    #Behaviour
    print(c)
#Function call
display()

#Function without parameters and with out return type
def sai(a,b):
    c = a + b
    print(c)
sai(1.2+.3,70)
#Function with parameters and with parameters
def msg(a,b):
    return a + b
res = msg(10,20)
print(res)


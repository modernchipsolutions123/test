"""
TYPES OF FUNCTIONS:
1.Positional arguments
2.Default arguments
3.Key word arguments

    1.Function with parameters and with return type
    2.Functions without parameters and with return type
    3.Functions with parameters and without return type
    4.Functions without parameters and without return type
"""
#1.Required Arguments/Positional Arguments : We can call in 3 ways.It will fallow the keywords
#2.Np.of arguments should be same in both function call and function deffination
def display(a,b = 20, c = 30):
    d = a + b + c
    print(d)
display(10)
display(20,30)
display(40,50,60)
display(1+10,1,3+2)

#2.Keyword /position Arguments: position is not required.we acan all 2 types
#Initilization will be done based on keyword(name)
def msg(x , y , z):
    s = x , y , z
    print(s)
msg("dhana","dhan","Dhanunjaya") # Without using keyword
msg(y = "Sai",x ="Gani",z = "Kadali") #By using keyword

#3.Default Arguments:No.of arguments need not be match with both function call and fnction deffinaion
    #2.Some of the aruments will be consider as default arguments
def dis(name,course="M.C.A"):
    print(name)
    print(course)
dis(name = "K.S.G",course ="B.S.C")
dis(name="M.P.C")





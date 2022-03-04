#**kargs :It allow us to pass variable no.of keyword argument like this
'''fun_name(name = 'Dhane',team='Kabadi')
1.It is same as dictionary
'''
def my_three(a,b,c):
    print(a,b,c)

a = {"a":1,"b":2,"c":3}
my_three(**a)

def my_func(**kargs):
    for i,j in kargs.items():
        print(i,j)
my_func(name = 'Dhana',sport = 'Kabadi',roll = 10, Height = 5.8)

def display(farg,**kwargs):
    #To display given values
    print("Formal arguments:",farg)
    for i,j in kwargs.items():
        print('key = {},value = {}'.format(i,j))
display(5,rno = 10)
display(5,area = 'AECS' , name = "Dhanunjay")


#Generators: It is used to generate sequence of values
            #2.It is an special type of functions.It is same as normalfunctions.It use return statement
            #3.In generator we use yield statement

'''#Print table:
def table(num):
    for i in range(1,11):
        print(f'{num} X {i} = {num * i}')
        #print(num,"X ",i,"=",num*i)
table(5)
#Simple Function
def table(num):
    for i in range(1,11):
        return f'{num} X {i} = {num * i}'
print(table(5))'''
# GENERATOR :
def table(num):
    for i in range(1,11):
        yield f'{num} X {i} = {num * i}'
g1 = table(9)
print(g1) #It will print reference of an object
for val in g1:
    print(val)
#Variable length Arguments :
'''
1.Arbitrary no.of arguments
2.By plaing * as prefix to the argument of function deffination
'''
def display(*Courses):
    for i in Courses:
        print(i)
display("M.C.A","B.S.C","M.P.C","S.S.C")

def msg(*School):
    for i in School:

        print(i)
msg("K.R.P","NRI","C.R.R","G.V.P")

def dis1(*a):
    for i in a:
        print(i)
dis1(10,20,30,40,40,60,70,80,90)
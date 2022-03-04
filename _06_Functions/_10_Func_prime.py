#3.print prime nbrs
#PRIME NUMBERS: Prime numbers is a natural number greater than 1 that has no positive divisiors other than 1 and itself
'''num = int(input("Enter any +ve nbr to check weather it is prime or not:"))
#2.Check the nbm is greater than 1
if num > 1:
    #4.check the prime numbers
    for i in range(2,num):

        # 3.Check the number is prime or not
        if num%i == 0:
            print(num,"Is not prime number")
            break
    else:
        print(num,"is a prime number")
'''

#1.Starting number
start = int(input("Enter the first nbr:"))
#2.Ending number
end = int(input("Enter the last nbr:"))
'''for i in range(start,end+1):
    #3.Prime nbr allways greater than 1
    if i > 1:
        #4.Prime nbs not divided by 1 and itself
        for j in range(2,i):
            #5.Check the condition if i divided by j becomes 0
            if i%j == 0:
                break
        else:
            print(i)'''

def prim_nbr(start,end):
    for i in range(start,end):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i)
prim_nbr(start,end)




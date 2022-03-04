#Largest number of the list by using oops concept
class Smallestest_nbr:
    def __init__(self):
        pass
    def small(self):
        n = int(input("Enter how many numbers :"))
        smallest = 0
        list1 = []
        print("Enter",n,"numbers")
        for i in range(n):
            num = int(input())
            list1.append(num)
            if smallest > num:
                smallest = num
        print(list1)
        print(min(list1))
smal1 = Smallestest_nbr()
smal1.small()

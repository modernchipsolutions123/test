#By using in-built method
li1 = [10, 20, 4, 45, 99]
print("Maximum nbr of list by using in-built:",max(li1))

class Largest_nbr:
    def __init__(self):
        pass
    def large(self):
        n = int(input("Enter how many numbers :"))
        largest = 0
        list1 = []
        print("Enter",n,"numbers")
        for i in range(n):
            num = int(input())
            list1.append(num)
            if largest < num:
                largest = num
        print(list1)
        print(max(list1))
        print("Largest Number: ",largest)
lar1 = Largest_nbr()
lar1.large()


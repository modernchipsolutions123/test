
try:
    n = int(input("Enter how many numbers :"))
    largest = 0
    list1 = []
    print("Enter", n, "numbers")
    for i in range(n):
        num = int(input())
        list1.append(num)
        if largest < num:
            largest = num
    print(list1)
    print(max(list1))
    print("Largest Number: ", largest)
except:

    print("Largest Number: ", largest)

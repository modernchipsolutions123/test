n = int(input("Enter the number: "))
def fib(n):
    first = 0
    second = 1
    for i in range(n):
        print(first)
        temp = first
        first = second
        second = first + second
fib(n)

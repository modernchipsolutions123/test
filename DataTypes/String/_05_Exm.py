
for i in range(101):
    print(i)
    if (i%3 == 0) and ( i%5 == 0):

        print("Buzz")
        print("fizz")
    elif i % 3 == 0:
        print(" fizz")
    elif i% 5 == 0:
        print("Buzz")
    else:
        print("It is false")

def simple():
    for i in range(20):
        if (i % 2 == 0):
            yield i

        # Successive Function call using for loop

for i in simple():
    print(i)  
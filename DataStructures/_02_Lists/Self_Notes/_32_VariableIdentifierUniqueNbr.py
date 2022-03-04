#36.Variable unique identification number
def f1(x):
    yield x
    yield x**3
    yield x**4
print(f1(5))
for j in f1(5):
    print(j)

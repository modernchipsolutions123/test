#Generator is same as functions,In generators we use Yield statement.In functions we use return statement.
def table(n):
    for i in range(1,11):
        yield f'{n} X {i} = {n * i}'
t1 = table(5)
for i in t1:
    print(i)
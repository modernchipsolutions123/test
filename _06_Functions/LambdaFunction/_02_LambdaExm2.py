'''def myfunc(n):
  return lambda a : a * n + 2

mydoubler = myfunc(5)

print(mydoubler(11))
'''

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(15))


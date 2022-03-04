'''
SELF :Self is not a keyword,We can use any name,But it is recommanded to use self.
      1.self is a reference variable,Which is always pointing to current object,
       Within the python class ,to acess current object,we can use self
       2.The first argument to the constructer is always self
	   3.The first argument to the Instance method is always self
		  We are not required to provide value for self variable

'''
class Test:
    def __init__(self):
        print("Address of object refered by self:", id(self))

t1 = Test()
print("Address of object refered by t1:",id(t1))

t2 = Test()
print("Address of object refered by t2:",id(t2))

class Test1:
    def __init__(x):
        print("Constructor:", id(x))

t1 = Test1()
print("Address of object refered by t1:",id(t1))


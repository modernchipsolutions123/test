'''
ENCAPSULATION : Wrapping(Binding3) of data members and  methods into an single entity
        Ex: Class:
'''
class EncapExm:
    #Constructor: It is used to initialize the instance variables
    def __init__(self):
        #Public : It can acess anywhere
        self.a = 10
        #Private : It can aces only in this method(__)
        self.__b = 20
        #Protect :
        self._c = 30

    def display(self):
        print(self.a + self.__b + self._c)

e1 = EncapExm()

e1.display()
print(e1.a)
print(e1._c)

'''list = [10,20,3,40,50]
print(sum(list))
sum = 0
for i in list:
    sum+=i
print(sum)
'''



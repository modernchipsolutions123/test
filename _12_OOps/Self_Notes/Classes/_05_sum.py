class Add:
    #1.STATE :

    def __init__(self, a, b):   #Constructor : It is used to initialize instance variables
        #Instance Variables
        self.a = a
        self.b = b

    #2.BEHAVIOUR :

    def display(self):   #Instance Method :
        print("Sum of two numbers....")
        # print(self.a+self.b)
        return self.a + self.b


s = Add(10, 20)
print(s.display())

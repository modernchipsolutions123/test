class Employee:
    #Class Variable :A variable which is inside the class outside the method. We can call anywhere
    a = 10
    b = 20

        #BEHAVIOUR
        #METHODS : A function which is inside the class and outside the method
        #Instance Method : By using self keyword we call as instance method
    def display(self):
        print(self.a )
        print(self.b)
    #Class Method :
    @classmethod
    def message(cls):
        print("this is class method")
e = Employee()
e.display()
Employee.message()


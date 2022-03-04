class InsMethod:
    #A method which is declared with self keyword .By using that self keyword we initialize the instance variables
    def display(self):
        self.name = "Sravani"
        self.salary = 200000
        self.age = 29
Im = InsMethod()
Im.display()
print(Im.__dict__)
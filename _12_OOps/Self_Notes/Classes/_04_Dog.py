class Dog:
    # 1.STATE
    # 1.1 Constructor : It is used to initialize the instance variables
    def __init__(self, breadname, color, legs):  # Fields
        self.breadname = breadname
        self.color = color
        self.color = color
        self.legs = legs

    # 2.Methods
    def display(self):
        print("Dog details....")
        print(self.breadname, self.color, self.legs)


d1 = Dog("Rajapalyam", "brown", 4)
d1.display()

class Car:
    def __init__(self, id, modelname, year):
        # 1.STATE
        self.id = id
        self.modelname = modelname
        self.year = year
        # 2.BEHAVIOUR

    def display(self):
        print("Car Details....")
        print(self.id, self.modelname, self.year)


c1 = Car(10, "Name:KIA", 'ModelNO:2019')  # 2.C1 is an object of a class car
c1.display()



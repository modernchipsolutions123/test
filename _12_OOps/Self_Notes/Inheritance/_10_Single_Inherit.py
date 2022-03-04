class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("Animal Speaking")
    def eating(self):
        print("Animals Eating")
#child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
    def eating(self):
        print("Dog Eating")
d = Dog() #It will print both methods in this child class
d.bark()
d.speak()
d.eating()

a = Animal()
a.speak()
#a.bark() AttributeError: 'Animal' object has no attribute 'bark'



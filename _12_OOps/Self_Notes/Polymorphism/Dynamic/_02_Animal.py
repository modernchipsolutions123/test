class Animal:
    #Class Variable : By using className and object reference
    eat = 'eating'
    #Instance Method : THis method is used by SELF keyword
    def get_msg(self):
        print("Animal was sleeping",Animal.eat)

# Child class Dog inherits the animal class
class Dog(Animal):
     def get_msg(self):
         print("Dog was barking")
d = Dog()
d.get_msg()
print(d.eat)




#Use same method in all the classes
class Class1:
    def m(self):
        print("this instance method In Class1")
    def s(self):
        print("class1")
class Class2(Class1):
    def m(self):
        print("this instance method In Class2")
    def s(self):
        print("class2")
class Class3(Class2):
    def m(self):
        print("this instance method In Class3")
    def s(self):
        print("class3")
class Class4(Class3):
    def m(self):
        print("class4")
c4 = Class4()
c4.m()
c4.s()

#class Grandfather():

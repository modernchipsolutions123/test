class Father_override:

    def __init__(self):  # SELF : it is used to contain memoryaddress of instance of currentclass
        self.property = 8000000.00
    #OVERRIDE : Both parent and child class hass same method name
    def display_property(self):
        print('Fathers Property =', self.property)

    def display_msg(self):
        print("This is child class")


class Son(Father_override):

    def __init__(self):

        self.property = 9000000.00

    def display_property(self):
        print('son\'s Property =', self.property)

    def display_msg(self):
        print("This is child class")

s = Son()
s.display_property()
s.display_msg()




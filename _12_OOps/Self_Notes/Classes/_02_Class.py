#CLASS : class is a (Design) blueprint or template
class Dance:
    #1.__init__ method is used to intiallize the attributes
    def __init__(self,institutename, year,numbers):
        # 1.STATE
        #1.1 Self is used to instance variables
        self.institutename = institutename #Fields
        self.year = year
        self.numbers=numbers

    '''def display(self):   #Methods
        print("DANCE INSTITUTE....")
        print(self.institutename, self.year, self.numbers)'''

    #2.d1 is an object :object is an instance of an class
d = Dance("KADALIROCZZ",2008,100) # d1 is an object of a class (Dance)
#d1=Dance("PADDINTLAMA CLASSICAL",1995,50)
#d.display()
#d1.display()
print(d)



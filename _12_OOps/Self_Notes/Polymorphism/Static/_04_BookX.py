class BookX:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages ,other.pages

class BookY:
    def __int__(self,pages):
        self.pages = pages
b1 = BookX(100,2,1)
b2 = BookY(200,2,1)
#Overloading : + operator acts as an objects
print('Total Pages :', b1+b2 )
print('Total pages :',b1-b2)

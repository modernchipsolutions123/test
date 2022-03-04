class Mul_list:
    def __init__(self):
        self.l1 = [2,4,6,8,1]
        self .l2 = 2
        self.l3 = [3]
    def display(self):
        try:
            print(self.l1,"It will multiply:",self.l1*2,"It will repeated:",self.l3,self.l1+self.l3)
            print(self.l1 * self.l3)
        except:
            print("Error occured in try")
mul1 = Mul_list()
mul1.display()

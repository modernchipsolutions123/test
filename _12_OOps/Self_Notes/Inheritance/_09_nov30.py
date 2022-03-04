#SINGLE INHERITANCE :
dic1 = {'A':{'id':1,'name':'Sai','Salary':{'B.A':1000,'S.A':1000,'H.R':1000}}}
dic2 = {'fname':'Sai','lname':'ganesh','location':'Vizag'}

class EmployeeA:

    # 2.Constructor :Used to initialize the instance variables
    def __init__(self, dic1):  # self keyword :Current object
        # Instance variables
        self.id = dic1['A']['id']
        self.name = dic1['A']['name']
        self.salary = dic1['A']['Salary']['B.A'] + dic1['A']['Salary']['S.A'] + dic1['A']['Salary']['H.R']
        # print(self.salary)

    # Create Method : A function inside the class is called method
    def salary_disp(self):
        print(self.id, self.name, self.salary)

dic2 = {'fname':'Sai','lname':'ganesh','location':'Vizag'}
class EmployeeB(EmployeeA):
    def __init__(self,dic1,dic2):
        #super():super method is used to call all instance variables from parent
        super().__init__(dic1)
        self.fname = dic2['fname']
        self.lname = dic2['lname']
        self.location = dic2['location']
    def emp_location(self):
        print(self.fname,self.lname,self.location)

#emp1 = EmployeeB(dic1)
#emp1.salary_disp()
emp2 = EmployeeB(dic1,dic2)
emp2.emp_location()
emp2.salary_disp()

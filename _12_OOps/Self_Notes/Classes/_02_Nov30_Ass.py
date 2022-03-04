dic1 = {'A':{'id':1,'name':'Sai','Salary':{'B.A':1000,'S.A':1000,'H.R':1000}}}
dic2 = {'fname':'Sai','lname':'ganesh','location':'Vizag'}
#print("Dictionary of items: ",dic1.items())
#print("Values of dic: ",dic1.values())
#print("Keys of dic :",dic1.keys())
# 1.Create class
class EmployeeA:
    # 2.Constructor :Used to initialize the instance variables
    def __init__(self,dic1):  # self keyword :Current object
        # Instance variables
        self.id = dic1['A']['id']
        self.name = dic1['A']['name']
        self.salary = dic1['A']['salary']['B.A'] + dic1['A']['salary']['S.A'] + dic1['A']['salary']['H.R']
        #Create Method : A function inside the class is called method
    def salary_basic(self):
        print(self.id,self.name,self.salary)

emp1 = EmployeeA(dic1)
emp1.salary_basic()

      #for i in dic1.items():
            #print()
'''
#def salary(self):
class EmployeeB:
  def __init__(self,dic2):
      self.fname = dic2['fname']
      self.lname = dic2['lname']
      self.location = dic2['location']
  def location_display(self):
      return dic2'''

#Object(a) -->Instance of a class
#emp = EmployeeA(dic1)
#emp.salary_basic()
#print(emp)

class Savings:

    def func_1(self):
        name =input("Enter the name :")
        eid = int(input("Enter the eid :"))
        months = int(input("Enter the no.of months :"))
        l1 = []
        for i in range(1, months + 1):
            salary =float(input("Enter the salary :"))
            basic = float(input("Enter the basic_allowance :"))
            special =float(input("Enter the special_allowance:"))
            tax = float(input("Enter the tax :"))
            total = (salary + basic + special )- tax
            print(total)
            l1.append(total)
            print("Final salary :",sum(l1))

            if total > 1:

                print("Win")
            else:
                    print("Fail")


    def fuc_2(self):
        dic1 = {}

        net = int(input("Enter the Expenditure: "))

        for j in range(1,net+1):

            key1 = input("Enter the name:")
            value1 = float(input("Enter the  cost:"))
            dic1[key1] = value1
            print(dic1)

            t1 = sum(dic1.values())
            print("total savings:",t1)




a = Savings()
a.func_1()
a.fuc_2()
'''
flag = True
while flag:
    if True:
        flag == True
    if False:
        flag == False
expence = input("Please enter name  of expence :")
cost = input("please enter cost of the expence:")    
n = input("Do u have any other expence:")
if yes:
    print("t")    
if No:
    print("f")'''






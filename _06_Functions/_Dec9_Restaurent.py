#Hotel real time example
print("\t\t\t ******Dhanadhan_Lovely_Non-veg******")
print("\t\tMenu\n1.Break fast\n2.Lunch\n3.Dinner")
oprt = 'y'
while(oprt is 'y'):
    #Optional is used to select to coustemer
    opt1 = int(input("Please enter your choice(1,2,3): "))
    if(opt1 == 1):
        print("Puri with special_chicken ")
    elif(opt1 == 2):
        print("Chicken receipe with mougal Biriyani")
    elif (opt1 == 3):
        print("Chicken Drum-Stick Biriyani")
    else:
        print("Invalid option")
    opt = input("Sir/Madam! Do you want order again(Yes/No)")


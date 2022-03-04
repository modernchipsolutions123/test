#1.Ask user for input integers
#2.Convert to list
#3.Given user output list
#4.Given input inegers as list in pairs
#5.print in a list

class Except:
    list1 = []
    while(True):
        try:
            nbr = input("Enter the number : ")
            if(nbr =='exit'):
                break
            else:
                list1.append(int(nbr))
        except:
            print("Enter numbers only.")

    print(list1)
e1 = Except()
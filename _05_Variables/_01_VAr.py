'''
#VARIABLE : Varaiable is name given to the memory location
A python variable is a reserved memory location to store values.In other words,
a variable in a python program gives data to the computer for processing
person_name = "Sai"
Fav_color = "Blue"
print("Person name :",person_name + " Likes ",Fav_color)
'''
name = input("What is your name :")
colour = input("Favourite color :")
print(name +" likes", colour)

#THis input() fuction is always treated as a string and we dont concatinate string to integer
#Ask a user their weight(in pounds),convert it to killograms
weight = input("Enter the weight :")
killograms = int(weight) * 0.45 #Converting weight into killograms
print("Converting weight into killo grams :",killograms)

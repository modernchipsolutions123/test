'''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  #print(x)
  if x == "banana":     #If the condition is true then it will break the condition
      break

  print("By using break statement:",x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
 # print(x)
  if x == "banana":         #If the condition is true then it will conditon the condition
      continue

  print("1.By using continue statement:",x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":         #If the condition is true then it will conditon the condition
      continue

  print("2.By using continue statement:",x)'''

print("..............")
#For loop with strings

str1 = "Hello World"
print(str1)
for char in str1:
    print(char)
print("End of for loop")

number = "12345"
for num in number: # it will iterate one by one
    print(num)

#2.For loop for list
print("----------------------")
# for loop with list

nbr = [1, '2', 3, 4, 5.8]
for value in nbr:
    print(value)
print("End for loop")

#2.1 String with list
nbr1 = ['1', 2, '3.5', '4', '5',2.89]
for value in nbr1:
    print(value)
print("End for loop")

str1 = ["Sai","Gani","Dhana"]
for i in str1:
    print(i)


#Tuple:
tp1 = (1 ,"sai",3 ,4 ,5)
for i in tp1:
    print(i)



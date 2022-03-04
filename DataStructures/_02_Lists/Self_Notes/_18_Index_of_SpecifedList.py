#22.Find index of an item in  specified list
#Stntax : list.index(element, start, end) #start, end is optional
num =['k', 'a', 'd', 'a', 'l', 'i']
print(num.index('a'))

my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print("The index of element C is ", my_list.index('C', 1, 5))
print("The index of element F is ", my_list.index('F', 3, 7))
#using just the startindex
print("The index of element D is ", my_list.index('D', 1))


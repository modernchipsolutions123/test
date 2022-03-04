# Getting square of even numbers from 1 to 10
squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]
# Display square of even numbers
print(squares)

# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
# Display list
print(List)

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:",list_using_comp)






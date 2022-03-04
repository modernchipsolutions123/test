'''#Without using list comprehension
matrix = []
for i in range(3):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)'''
# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)
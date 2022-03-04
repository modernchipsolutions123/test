'''n = [1,2,3,4]
print(sum(n))

#Without using functions
numbers = [1, 2, 3, 4, 5, 1, 4, 5]
# start parameter is not provided
Sum = sum(numbers)
print(Sum)
# start = 10
Sum = sum(numbers, 10)
print(Sum)'''

li1 = [1,2,-8]
def sum_list(li1):
    sum_numbers = 0
    for x in li1:
        sum_numbers += x
    return sum_numbers
print(sum_list(li1))
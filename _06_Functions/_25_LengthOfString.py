#A function to find total and average
def calculate(lst):
    #To find total and average
    n = len(lst)
    sum = 0
    for i in lst:
        sum += i
        avg = sum/n
        return sum,avg
#Take a group of integers from keyboard
print("Enter nubers separated by space:")
lst = [int(x) for x in input().split()]
x,y = calculate(lst)
print('Total:',x)
print('Avg:',y)



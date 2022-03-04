
num = int(input("Enter no.of subjects :"))
# list1_marks = []
# list2_sub = []
dic1 = {}
sum = 0
for i in range(num):
    sub_name = input("Enter the subject :")
    sub_marks = int(input("Enter the marks:"))

    dic1[sub_name] = sub_marks
print(dic1)

for i, j in dic1.items():
    print(i, j)
    sum = sum + j
avg = sum / num
print(avg)
count = 0
if avg < 75.0:
    if count == 3:

        if avg < 65 and avg > 75:
            print("GIVE A CHANCE")

else:

    print("FAILED")


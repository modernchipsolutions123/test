# 1. no of subjects, 2. subject names and 3. marks: user input
# total percentage if less than 75 % in 3 subjects chance again else failed (for 3-7)
# total per if between 65 to 75 chance again, less than 65 failed (above 7 subjects)
class Sub_Marks:
    def sub_Mark(self_):
        num = int(input("Enter no.of subjects :"))
        # list1_marks = []
        # list2_sub = []
        dic1 = {}
        sum = 0
        for i in range(1,num + 1 ):
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

sb1 =  Sub_Marks()
sb1.sub_Mark()

class Student_marks:

    def sub_between_3_to_7(self, n):
        marks_dict = dict()
        marks_list = []
        for i in range(1, n + 1):
            subject = input(f'enter the name of the subject {i} : ')
            # this checks if the marks are between 0 and 100
            while True:
                marks = int(input(f'enter the marks for the subject {subject} : '))
                if marks < 0 or marks > 100:
                    print('enter the marks between 0 and 100... : ')
                    continue
                marks_dict.update({subject: marks})
                marks_list.append(marks)
                break

        avg = (sum(marks_list)) / n

        # count number of subject whose marks are <= 75
        count = 0
        for i in marks_list:
            if i <= 75.0:
                count = count + 1

        print('\nResult : ', end=' ')
        if avg >= 90.0:
            print('Distinction')

        elif avg >= 75.0 and avg <= 90.0:
            print('Average')

        elif avg < 75.0:
            if count <= 3 and number > 3:
                print('passed')
            else:
                print('failed')

        print("\nyour marks list \n-----------------")
        for subject, marks in marks_dict.items():
            print(subject, ' : ', marks)
        print('\npercentage : {:.2f}%'.format(avg))


    def sub_more_than_7(self, n):
        marks_dict = dict()
        marks_list = []
        for i in range(1, n + 1):
            subject = input(f"enter the name of the subject {i} : ")
            # this checks if the marks are between 0 and 100
            while True:
                marks = int(input(f'enter the marks for the subject {subject} : '))
                if marks < 0 or marks > 100:
                    print('\nenter the marks between 0 and 100... : \n')
                    continue
                marks_dict.update({subject: marks})
                marks_list.append(marks)
                break

        avg = (sum(marks_list) / n)

        # count number of subjects whose marks are between 65 and 75
        count = 0
        for i in marks_list:
            if i >= 65.0 and i <= 75.0:
                count = count + 1


        print('\nResult : ', end='')
        if avg >= 90.0:
            print('Distinction')

        elif avg >= 75.0 and avg <= 90.0:
            print('Average')

        elif avg <= 75.0:
            if count == 3:
                print('Passed')

            elif count == 4:
                print('Failed')

            elif count >= 5:
                print('Debarred')

        print('\nyour marks list \n-----------------')
        for subject, marks in marks_dict.items():
            print(subject, ' : ', marks)
        print('\npercentage : {:.2f}'.format(avg))


number = 0
s1 = Student_marks()

while True:
    number = int(input('enter the number of subjects : '))
    if 3 <= number <= 7:
        s1.sub_between_3_to_7(number)

    elif number > 7:
        s1.sub_more_than_7(number)

    elif number < 3:
        print('\nminimum 3 subject, enter again...\n')
        continue
    break


# 1. no of subjects, 2. subject names and 3. marks: user input
# total percentage if less than 75 % in 3 subjects chance again else failed (for 3-7)
# total per if between 65 to 75 chance again, less than 65 failed (above 7 subjects)



def func1(self,n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input(f'enter the name of the subject {i} : ')
        marks = int(input(f'enter the marks for the {subject} : '))
        marks_dict.update({subject: marks})
        marks_list.append(marks)

    avg = (sum(marks_list)) / n

    count = 0
    for i in marks_list:
        if i >= 75.0:
            count = count + 1

    if avg >= 90.0:
        print('distinction')

    elif avg >= 75.0 and avg <= 90.0:
        print('average')

    elif avg < 75.0:
        if count >= 3:
            print('pass')
        else:
            print('failed')

    for i, j in marks_dict.items():
        print(i, ' : ', j)


def func2(self,n):
    marks_dict = dict()
    marks_list = []
    for i in range(1, n + 1):
        subject = input(f'enter the name fo the  subject {i}  : ')
        marks = int(input(f'enter the marks for the {subject} : '))
        marks_dict.update({subject: marks})
        marks_list.append(marks)

    avg = (sum(marks_list) / n)

    count = 0
    for i in marks_list:
        if i >= 65.0 and i <= 75.0:
            count = count + 1

    if avg >= 90.0:
        print('distinction')

    elif avg >= 75.0 and avg <= 90.0:
        print('average')

    elif avg <= 75.0:
        if count == 3:
             print('passed')

    elif count == 4:
        print('failed')

    elif count >= 5:
        print('debarred')

    for i, j in marks_dict.items():
        print(i, ' : ', j)


number = int(input('enter the number of subjects: '))

if 3 <= number <= 7:
    func1(number)

elif number > 7:
    func2(number)

elif number < 3:
    print('enter minimum subject 3')


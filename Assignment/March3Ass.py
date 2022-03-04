'''str1 = input("Enter the string:")
print(str1)
if str1 =="()":
    print("Given Paranthesis is valid")
else:
    print("Given Paranthesis is in-valid")
'''

str1 = ['()',')(()))','(','(())((()())())',')test','hi())(','(hello))','hello','(hell(0))']
for str_Paran in str1:
    stk = []
    flag = 1
    for letter in str_Paran:
        if(letter == '('):
            stk.append(letter)
        elif(letter == ')'):
            try:
                stk.pop()
            except:
                flag = 0
    if(flag == 1):
        if not stk:
            print(str_Paran," : ", True)
        else:
            print(str_Paran," : ",False)


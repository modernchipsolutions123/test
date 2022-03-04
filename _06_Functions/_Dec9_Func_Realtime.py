'''def func():
    print("This is function ")
func()
def func1(a,b):
    print(f'arguments are {a} and {b}')
    return a + b
res = func1(10,20)
print(res)'''

try:
    f = open("C:/Users/saiga/PycharmProjects/pythonProject/MCS-0048_MCS_Ganesh_Corepython/_06_Functions/_Dec9_Func_Realtime.py")
    print("Open the file",f)
except:
    print("Exception occur in try block")
finally:
    f.close()
    print("File is closed")

try:
    f = open("048_MCS_Ganesh_Corepython/_06_Functions/_Dec9_Func_Realtime.py")
    print("Open the file",f)
except:
    print("Exception occur in try block")


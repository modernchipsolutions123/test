#Python first prefernce will give to the Local variable scope
#LEGB-Rule : Local ---> Encloser ---> Global ---> Built-in
x = 30
def func(): #Encloser
    x =40
    def inner():
        x = 50
        print(x)
    inner()
func()
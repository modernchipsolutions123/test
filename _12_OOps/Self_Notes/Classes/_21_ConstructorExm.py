class Test:
    def __init__(self,name):
        self.name = name
t = Test("Sai")
print(t.name)
#Reinitialization
t.__init__('Kadali')
print(t.name)

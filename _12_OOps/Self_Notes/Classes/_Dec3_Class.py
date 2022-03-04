class Instance_VarMethod:
    #1.Class Variable
    #name = "Kadali"
    #2.Constructor/Method:It is  used to initialize the instance variables
    def __int__(self,fname,lname,id):
        #Instance Variable :  by using self keyword
        self.fname = fname
        self.lname = lname
        self.id = id
        #Instance method
   # def display_instance(self):
       # print(self.fname,self.lname,self.id)
a1 = Instance_VarMethod("Sai","Ganesh",1)
print(a1)
#a1.display_instance()

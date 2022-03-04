'''
GARBAGE COLLECTOR :
            1.It is used to destroy the useless object
            2.Without class and object in python garbagecollector is used
            ex: a = 10
            Because every thing printed as an object in python
            3.But python does not support all the oops features
            ex: overloading
            4.Garbage collector allways there in background execution whereever memory prbls will come
            5.If the object does not have any reference variable then gc(GarbageCollector) will form
            6.In python we import gc module
Destructor:
            Garbage collector is responsible to call the destructor before destroying the object to perform cleanup activities
            Once destructor execution is completed the G.C immediately destroy the object
            OBJECT---->CONSTRUCTOR---->USE THAT OBJECT---->DESTRUCTOR---->GC DESTROY THE OBJ

'''
import gc
class GcExm:
    def __init__(self):
        print("This is Constructor to perform to initialize")
    def __del__(self):
        print("This is destructor to perform cleanup activities")
gc1 = GcExm()
gc2 = gc1           #by using gc2,gc3 reference object garbage collector will for
gc3 = gc2
print("Objects no longer required")

'''gc = None #gc object has no refernce
# gc.isenabled() #False
gc.desable()
'''

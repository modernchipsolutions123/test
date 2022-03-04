#OVERLOADING : Compile-time
class Constructor_overloading:

    # constructor overloading
    def __init__(self, eid=10, name='gani', sal=1000):
        self.eid = eid
        self.name = name
        self.sal = sal
        print(self.eid, self.name, self.sal)

# Constructor Overloading : Same name with different input parameters at Run_time
gani = Constructor_overloading()
gani = Constructor_overloading(100)
ani = Constructor_overloading(101, 'gani kadali')
sai = Constructor_overloading(102, 'kadali sai', 20000)

class Addmem_set:
    def __init__(self,set):
        self.set = set
    def ele(self):
        for i in set:
            print(i)
        set.update(["12","15"])
        print(set)
set = set()
a = Addmem_set(set)
a.ele()
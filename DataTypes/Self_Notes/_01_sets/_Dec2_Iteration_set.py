class Iteration_set:
    def __init__(self,test):
        self.test = test
    def loop(self):
        for i in test:
            print(i)
test = set("this is MCS software company")
it1 = Iteration_set(test)
it1.loop()
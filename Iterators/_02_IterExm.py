class IterExm():
    def __iter__(self):
        self.x = 10
        return self.x
    def __next__(self):
        y = self.x
        self.x+= 1
        print(y)

print(IterExm())
#Iterxm = iter(oi)
#print(IterExm)


class PostalAddress:
    pass
    def dic_exm(self):
        #cP1 = PostalAddress()
        # Create an Instance for person ABC
        self.name = "ABC"
        self.street = "Central Street - 1"

        # Create an Instance for person DEF
        #cP2 = PostalAddress()
        self.name = "DEF"
        self.street = "Central Street - 2"
#print(cP1.__dict__)
#print(cP2.__dict__)
pa1 = PostalAddress()
pa1.dic_exm()
pa1.dic_exm()
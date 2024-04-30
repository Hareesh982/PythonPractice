class mom:  # Parent class
    def __init__(self, name):
        self.name = name

    def property(self):
        print("Jewellery")


class dad:  # Parent class
    def __init__(self, address):
        self.address = address

    def property(self):
        print("Flat")


class son(dad, mom):  # Child class
    def __init__(self, age):

        mom.__init__(self, "Laura")
        dad.__init__(self, "Mysore")
        self.age = age

    def property(self):
        mom.property(self)
        dad.property(self)
        print("Mobile")


Son = son(12)
Son.property()
    



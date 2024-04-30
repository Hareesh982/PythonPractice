class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return self.first+"."+self.last+"@gmail.com"

    def fullname(self):
        return self.first+" "+self.last

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

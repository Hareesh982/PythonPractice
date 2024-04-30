class Employee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@cognizant.com"
    
    def fullname(self):
        return self.first+" "+self.last

    def apply_raise_by_percentage(self):
        global raise_amount
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("Hareesh","D",875000)
emp_2 = Employee("Rajesh","D",700000)

print(Employee.fullname(emp_1), emp_1.pay)
print(Employee.fullname(emp_2), emp_2.pay)

Employee.apply_raise_by_percentage(emp_1)
Employee.apply_raise_by_percentage(emp_2)

print("after pay rise")

print(Employee.fullname(emp_1), emp_1.pay)
print(Employee.fullname(emp_2), emp_2.pay)







#find the no of employees or no of objects created
class Employee:
    raise_amount = 1.04
    no_of_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@cognizant.com"

        Employee.no_of_employees = Employee.no_of_employees + 1
    def fullname(self):
        return self.first+" "+self.last

    def apply_raise_by_percentage(self):
        global raise_amount
        self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee("hareesh","d",70000)
emp_2 = Employee("rajesh","d",60000)
emp_3 = Employee("asha","d",75000)

print(Employee.no_of_employees)
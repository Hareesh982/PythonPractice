#class and static methods
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

    @classmethod
    def fun(cls,emp_str):
        first,last,pay= emp_str.split("-")
        return Employee(first,last,pay)
    
    @staticmethod
    def fun_2(x):
        return x

emp_1 = Employee("Brent","Rivera",60000)
emp_2 = Employee("Lexi","Rivera",50000)
emp_3 = Employee("Dom","Brack",80000)

emp_4 = "lexi-hensler-60000"
emp_5 = "andrew-daviala-75000"

new_emp_1 = Employee.fun(emp_4)
new_emp_2 = Employee.fun(emp_5)

print(emp_1.email)
print(emp_1.pay)
print(emp_2.email)
print(emp_2.pay)
print(emp_3.email)
print(emp_3.pay)
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_2.email)
print(new_emp_2.pay)

print("No of employees : ", Employee.no_of_employees)

print(Employee.fun_2('hareesh'))



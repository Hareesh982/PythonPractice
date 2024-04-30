#magic and dunder


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@cognizant.com"

    def fullname(self):
        return self.first+" "+self.last

    def apply_raise_by_percentage(self):
        global raise_amount
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):
        return f"{self.fullname()} {self.pay}"

    def __str__(self):
        return f"{self.fullname()} {self.pay}"
    
    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Company(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if(employees == None):
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def total_emps(self):
        total = 0
        for emp in self.employees:
            print("---->", emp.fullname())
            total = total + 1
        return f"Total no of employees : {total}"

    def total_comb_sal(self):
        total_salary = 0
        for emp in self.employees:
            total_salary = total_salary + emp.pay
        return f"Total salary for all the employees : {total_salary}"


com = Company("Tata Consultancy services", ".pvt Ltd",1000000000,[])
emp_1 = Employee("Lexi", "Hensler", 60000)
emp_2 = Employee("Dom", "Brack", 55000)
emp_3 = Employee("Ben", "Azelert", 65000)
emp_4 = Employee("Sofie", "Dosie", 50000)
emp_5 = Employee("Brent", "Rivera", 60000)

com.add_emp(emp_1)
com.add_emp(emp_2)
com.add_emp(emp_3)
com.add_emp(emp_4)
com.add_emp(emp_5)

print(com.fullname())
print(com.total_emps())
print(com.total_comb_sal())
print()
print(str(emp_1))
print(repr(emp_1))
print(emp_1 + emp_2)
print(len(emp_1))





#Inheritance

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay, prog_lang):
        self.first = first
        self.last = last
        self.pay = pay
        self.prog_lang = prog_lang
        self.email = first+"."+last+"@gmail.com"

    def fullname(self):
        return self.first+" "+self.last

    def apply_raise_by_percentage(self):
        global raise_amount
        self.pay = int(self.pay * Employee.raise_amount)

class Manager(Employee):
    def __init__(self, first, last, pay, prog_lang, employees = None):
        super().__init__(first, last, pay, prog_lang)
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
        
    def print_emps(self):
        total = 0
        for emp in self.employees:
            print("---->",emp.fullname())
            total = total + 1
        return f"Total no of employees : {total}"

emp_1 = Employee("Lexi","Hensler",60000,"Java")
emp_2 = Employee("Dom","Brack",55000,"Python")
emp_3 = Employee("Ben","Azelert",65000,"Java")
emp_4 = Employee("Sofie","Dosie",50000,"C++")

emp_man = Manager("Brent","Rivera",100000,"Java",[])
print("Manager : ",emp_man.fullname())

emp_man.add_emp(emp_1)
emp_man.add_emp(emp_2)
emp_man.add_emp(emp_3)
emp_man.add_emp(emp_4)

print(emp_man.print_emps())








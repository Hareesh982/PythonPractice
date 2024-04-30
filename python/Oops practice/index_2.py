class Employee:

	raise_amount = 1.04
	no_of_emps = 0

	def __init__(self, first_name, last_name, salary, company_name):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
		self.company_name = company_name
		self.email = first_name + "." + last_name + "@" + company_name + ".com"
		Employee.no_of_emps +=1

	def fullname(self):
		return f"{self.first_name} {self.last_name}"

	def apply_raise(self):
		self.salary = int(self.salary * self.raise_amount)

print(f"No.of.Employees : {Employee.no_of_emps}") 

emp1 = Employee("Hareesh","Duddupudi",80000,"cognizant")
emp2 = Employee("Rajesh","Duddupudi",90000,"accenture")

print(f"No.of.Employees : {Employee.no_of_emps}")

print("Before Hike")
print(emp1.salary)

emp1.apply_raise()

print("After Hike")
print(emp1.salary)

print(emp1.__dict__)

Employee.raise_amount = 2.5
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print("----------")

emp1.raise_amount = 1.6
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

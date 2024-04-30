class Employee:
	def __init__(self, first_name, last_name, salary, company_name):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary
		self.company_name = company_name
		self.email = first_name + "." + last_name + "@" + company_name + ".com"

	def fullname(self):
		return f"{self.first_name} {self.last_name}"


emp1 = Employee("Hareesh","Duddupudi",80000,"cognizant")
emp2 = Employee("Rajesh","Duddupudi",90000,"accenture")

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(Employee.fullname(emp1))
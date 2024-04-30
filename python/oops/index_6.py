#Basic calculator using class

class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num2 - self.num1
    
    def multi(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2

x = input("Enter the first number : ")
y = input("Enter the second number : ")
if("." in x):
    x = float(x)
else:
    x = int(x)
if("." in y):
    y = float(y)
else:
    y = int(y)

obj = calculator(x,y)

choice = 1
while(choice != 0 ):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice = int(input("Enter the choice : "))
    if(choice == 1):
        print("Result :", obj.add())
    elif(choice == 2):
        print("Result :", obj.sub())
    elif(choice == 3):
        print("Result :", obj.multi())
    elif(choice == 4):
        print("Result :", obj.div())
    elif(choice == 0):
        break
    else:
        print("invalid choice")
    print("--------------")

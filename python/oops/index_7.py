#Python Program to Append, Delete and Display Elements of a List using Classes

class structure:
    def __init__(self,values = None):
        if(values == None):
            self.values = []
        else:
            self.values = values
    def add_value(self,value):
        self.values.append(value)
    def remove_value(self,value):
        self.values.remove(value)
    def print_value(self):
        return self.values
    
obj = structure([])

choice = 1
while(choice != 0):
    print("1.Append")
    print("2.Remove")
    print("3.List values")
    choice = int(input("Enter the choice : "))
    if(choice == 1):
        x = input("Enter the value to append : ")
        if x.isalpha():
            x = x
        elif("." in x):
            x = float(x)
        else:
            x = int(x)
        obj.add_value(x)
    elif(choice == 2):
        y = input("Enter the value to remove : ")
        if(y not in obj.print_value()):
            print("value not in the list")
        else:
            obj.remove_value(y)
    elif(choice == 3):
        print(obj.print_value())
    elif(choice == 0):
        break
    else:
        print("invalid choice")
    print("--------------")

# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def Perimeter(self):
        return 2*(self.width + self.length)
    
    def Area(self):
        return self.length * self.width
    
    def display(self):
        print("Length of a rectangle : ", self.length)
        print("Width of a rectangle : ", self.width)
        print("Perimeter of a rectangle : ", self.Perimeter())
        print("Area of a rectangle : ", self.Area())
        

class Parallelepipede(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.Area() * self.height


x = int(input("Enter the length : "))
y = int(input("Enter the width : "))
z = int(input("Enter the heigh : "))
obj = Rectangle(x,y)
obj.display()

print("----------------------------------")
myParallelepipede = Parallelepipede(x,y,z)
print("the volume of myParallelepipede is: ", myParallelepipede.volume())



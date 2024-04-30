class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"name : {self.name}")
        print(f"age : {self.age}")

    def get_info(self):
        print(f"coat_color : {self.coat_color}")
    
class JackRussellTerrier(Dog):
    def speak(self):
        print("urrrrr")

    def walk(self):
        print("walking")

class Bulldog(Dog):
    def run(self):
        print("running")
    
    def speak(self):
        print("awaw")


obj_1 = JackRussellTerrier("jojo", 5, "Brown")
obj_2 = Bulldog("Browny",4,"Black")

obj_1.description()
obj_1.get_info()
obj_1.speak()
obj_1.walk()

print()

obj_2.description()
obj_2.get_info()
obj_2.run()
obj_2.speak()





# Question-9
# Write a program to reverse a stack.

class stack:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return self.array == []
    
    def push(self, data):
        self.array.append(data)
    
    def pop(self):
        return self.array.pop()

    def show(self):
        for i in reversed(self.array):
            print(i)
    
def insert(obj, data):
    if obj.is_empty():
        obj.push(data)
    else:
        p = obj.pop()
        insert(obj, data)
        obj.push(p)
    
def reverse(obj):
    if not obj.is_empty():
        p = obj.pop()
        reverse(obj)
        insert(obj, p)
        

obj = stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)

print("Original Stack : ")
obj.show()
reverse(obj)
print("Reversed Stack : ")
obj.show()



#***********************OUTPUT************************

# Original Stack:
# 50
# 40
# 30
# 20
# 10
# Reversed Stack:
# 10
# 20
# 30
# 40
# 50

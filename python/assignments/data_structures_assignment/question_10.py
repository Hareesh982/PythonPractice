# Question-10
# Write a program to find the smallest number using a stack.

class stack:
    def __init__(self):
        self.array = []
    
    def push(self,data):
        self.array.insert(0,data)
    
    def pop(self):
        if len(self.array) == 0:
            return "Stack is empty"
        self.ele = self.array[0]
        self.array.pop(0)
    
    def peek(self):
        if len(self.array) == 0:
            return "Stack is empty"
        self.top = self.array[0]
    
    def smallest_ele(self):
        for i in range(len(self.array)-1):
            self.pop()
            self.peek()
            x = self.ele
            if x < self.top:
                self.pop()
                self.push(x)
        self.peek()
        print("smallest element of a stack is ",self.top)
        

obj = stack()
obj.push(10)
obj.push(14)
obj.push(6)
obj.push(20)
obj.push(11)

obj.smallest_ele()



#*************************OUTPUT************************

# smallest element of a stack is 6


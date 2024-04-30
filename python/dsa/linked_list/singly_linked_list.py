
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.Traverse()

    def insert_at_end(self, data):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        newNode = Node(data)
        temp.next = newNode
        self.Traverse()

    def insert_at_pos(self, pos, data):
        newNode = Node(data)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
            self.Traverse()
        else:
            current = self.head
            previous = None
            i = 0
            while i < pos:
                previous = current
                current = current.next
                i = i + 1
            previous.next = newNode
            newNode.next = current
            self.Traverse()

    def delete_at_begin(self):
        self.head = self.head.next
        self.Traverse()

    def delete_at_end(self):
        current = self.head
        previous =  None
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        self.Traverse()

    def delete_at_pos(self, pos):
        previous = None
        current = self.head
        i = 0
        while i < pos:
            previous = current
            current = current.next
            i = i + 1
        previous.next = current.next
        self.Traverse()
        
    def Traverse(self):
        temp = self.head
        print()
        while temp:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next
        print("None\n")

if __name__ == "__main__":
    l = linked_list()
    while True:
        print("1.Insert at begin")
        print("2.Insert at position")
        print("3.Insert at end")
        print("4.Delete at begin")
        print("5.Delete at position")
        print("6.Delete at end")
        print("0.Exit")
        choice = int(input("Enter the choice : "))
        if choice == 1:
            data = int(input("Enter the data : "))
            l.insert_at_begin(data)
        elif choice == 2:
            data = int(input("Enter the data : "))
            position = int(input("Enter the position : "))
            l.insert_at_pos(position,data)
        elif choice == 3:
            data = int(input("Enter the data : "))
            l.insert_at_end(data)
        elif choice == 4:
            l.delete_at_begin()
        elif choice == 5:
            position = int(input("Enter the position : "))
            l.delete_at_pos(position)
        elif choice == 6:
            l.delete_at_end()
        elif choice == 0:
            break
        else:
            print("Invalid choice")
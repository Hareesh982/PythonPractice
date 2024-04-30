
# Question - 4
# Function to print all the leaves in a given binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def insert(self,node,data):
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left,data)
            else:
                node.right = self.insert(node.right,data)
        return node
    
    def print_leaves(self,root):
        if root is not None:
            if root.left is None and root.right is None:
                print(root.data,end = " ")
            else:
                self.print_leaves(root.left)
                self.print_leaves(root.right)

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

print("Leaves of binary tree : ",end = " ")
tree.print_leaves(root)


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# Leaves of binary tree :  1 3 7 9



# Question - 3
# Perform Pre-order, Post-order, In-order traversal

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

    def in_order_traversal(self,root):
        if root is not None:
            self.in_order_traversal(root.left)
            print(root.data, end=" ")
            self.in_order_traversal(root.right)

    def pre_order_traversal(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self,root):
        if root is not None:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data, end=" ")

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

print("Root node : ",root.data)
print()

print("In_order_traversal : ",end = " ")
tree.in_order_traversal(root)
print("\n")

print("Pre_order_traversal : ",end = " ")
tree.pre_order_traversal(root)
print("\n")

print("Post_order_traversal : ",end = " ")
tree.post_order_traversal(root)
print("\n")


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# Root node :  6

# In_order_traversal :  1 2 3 6 7 8 9 

# Pre_order_traversal :  6 2 1 3 8 7 9 

# Post_order_traversal :  1 3 2 7 9 8 6


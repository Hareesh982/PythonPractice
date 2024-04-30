
# Question - 10
# Print the nodes at odd levels of a tree

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
    def print_nodes_at_odd_levels(self,root, level=1):
        if root is None:
            return

        if level % 2 == 1:
            print(root.data, end=" ")

        self.print_nodes_at_odd_levels(root.left, level+1)
        self.print_nodes_at_odd_levels(root.right, level+1)

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

print("Nodes at odd levels : ",end = " ")
tree.print_nodes_at_odd_levels(root)


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# Nodes at odd levels :  6 1 3 7 9


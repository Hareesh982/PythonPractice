
# Question - 7
# Find sum of all nodes of the given perfect binary tree

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
    
    def sum_of_nodes(self,root):
        if root is None:
            return 0

        return (root.data + self.sum_of_nodes(root.left) + self.sum_of_nodes(root.right))


root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

sum = tree.sum_of_nodes(root)
print("Sum of all nodes of the given perfect binary tree : ",sum)


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# Sum of all nodes of the given perfect binary tree :  36


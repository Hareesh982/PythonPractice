
# Question - 2
# Find height of a given tree

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
    def height(self,root):
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return max(left_height, right_height) + 1

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

high = tree.height(root)
print("Height of a given tree is :",high)


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# Height of a given tree is : 3


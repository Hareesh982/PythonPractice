
# Question - 8
# Count sub tress that sum up to a given value x in a binary tree

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
    def count_subtrees_with_sum(self,root, x):
        if root is None:
            return 0

        count = 0
        if root.data == x:
            count += 1

        count += self.count_subtrees_with_sum(root.left, x - root.data)
        count += self.count_subtrees_with_sum(root.right, x - root.data)

        return count

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

sum_value = int(input("Enter the sum value : "))
count = tree.count_subtrees_with_sum(root,sum_value)
print(f"Number of subtrees with sum {sum_value} : ", count)


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9

# -----------OUTPUT----------

# Enter the sum value : 8
# Number of subtrees with sum 8 :  1


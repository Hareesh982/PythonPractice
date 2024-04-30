
# Question - 9
# Find maximum level sum in Binary Tree

from collections import deque
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
    def max_level_sum(self,root):
        if root is None:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        level_with_max_sum = 0
        level = 1

        while queue:
            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.data

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                level_with_max_sum = level

            level += 1

        return level_with_max_sum

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)

maximum_sum = tree.max_level_sum(root)
print("Level with maximum sum is : ",maximum_sum)



# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# Level with maximum sum is :  3


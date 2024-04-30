
# Question - 5
# Implement BFS (Breath First Search) and DFS (Depth First Search)

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
    def dfs_traversal(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.dfs_traversal(root.left)
            self.dfs_traversal(root.right)

    def bfs_traversal(self,root):
        if root is None:
            return
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

root = Node(6)
tree = Tree()

tree.insert(root,2)
tree.insert(root,1)
tree.insert(root,3)
tree.insert(root,8)
tree.insert(root,7)
tree.insert(root,9)


print("DFS traversal : ",end = " ")
tree.dfs_traversal(root)

print()

print("BFS traversal : ",end = " ")
tree.bfs_traversal(root)


# tree format
#        6
#      /   \
#     2     8
#    / \   / \
#   1   3 7   9


# -----------OUTPUT----------

# DFS traversal :  6 2 1 3 8 7 9 
# BFS traversal :  6 2 8 1 3 7 9


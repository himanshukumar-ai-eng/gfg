'''Tree node structure
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def deleteNode(self, root, k):
        if root is None:
            return None
        if root.data >= k:
            return self.deleteNode(root.left, k)
        root.right = self.deleteNode(root.right, k)
        return root

        
        
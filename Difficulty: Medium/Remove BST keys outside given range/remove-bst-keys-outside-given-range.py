'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        if root is None:
            return None
        left = self.removekeys(root.left,l,r)
        right = self.removekeys(root.right,l,r)
        
        if root.data < l:
            return right

        if root.data > r:
            return left

        root.left = left
        root.right = right

        return root
        
       
        
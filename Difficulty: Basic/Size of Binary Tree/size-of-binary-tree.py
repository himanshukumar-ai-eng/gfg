"""
Definition for Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def getSize(self, root):
        q = deque([root])
        count = 0
        while q:
            root = q.popleft()
            count += 1
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
        return count
                
        
     
        
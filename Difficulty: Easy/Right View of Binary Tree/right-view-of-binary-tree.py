'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self, root):
        result = []
        if root is None:
            return result
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                curr = q.popleft()
                if i == level_size - 1:
                    result.append(curr.data)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
        return result
        
        
        
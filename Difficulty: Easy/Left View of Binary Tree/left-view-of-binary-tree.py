''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def rectleftView(self,root,level,res):
        if root is None:
            return 
        if level == len(res):
            res.append(root.data)
        self.rectleftView(root.left, level + 1, res)
        self.rectleftView(root.right, level + 1, res)
    def leftView(self, root):
        res = []
        self.rectleftView(root,0,res)
        return res
        # code here
        
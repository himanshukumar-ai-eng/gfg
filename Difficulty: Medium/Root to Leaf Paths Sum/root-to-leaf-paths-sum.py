# Structure of a Tree Node
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def solve(self,root,currentnumber):
        if root is None:
            return 0
        currentnumber = currentnumber * 10 + root.data
        if root.left is None and root.right is None:
            return currentnumber
        return (self.solve(root.left,currentnumber) + self.solve(root.right,curremtnumber))
        
    def treePathsSum(self, root):
        return self.solve(root,0)
        # code here.
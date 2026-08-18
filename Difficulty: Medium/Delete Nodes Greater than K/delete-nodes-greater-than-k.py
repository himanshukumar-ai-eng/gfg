class Solution:
    def deleteNode(self, root, k):
        if root is None:
            return None
            
        if root.data >= k:
             return self.deleteNode(root.left, k)
             
        root.left = self.deleteNode(root.left, k)
        root.right = self.deleteNode(root.right, k)
        return root

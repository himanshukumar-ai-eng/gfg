class Solution:
    def findCeil(self, root, x):
        if root is None:
            return -1

        if root.data == x:
            return root.data

        if root.data < x:
            return self.findCeil(root.right, x)

        ceil = self.findCeil(root.left, x)

        if ceil >= x:
            return ceil
        else:
            return root.data
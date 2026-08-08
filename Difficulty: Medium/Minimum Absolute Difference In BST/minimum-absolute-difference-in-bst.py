class Solution:
    def inorder(self, inord, root):
        if root is None:
            return

        self.inorder(inord, root.left)
        inord.append(root.data)
        self.inorder(inord, root.right)

    def absolute_diff(self, root):
        inord = []

        self.inorder(inord, root)

        mini = float('inf')
        n = len(inord)

        for i in range(n - 1):
            mini = min(mini, inord[i + 1] - inord[i])

        return mini
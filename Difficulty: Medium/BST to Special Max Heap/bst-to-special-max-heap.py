class Solution:

    def inorderTraversal(self, root, arr):
        if root is None:
            return

        self.inorderTraversal(root.left, arr)
        arr.append(root.data)
        self.inorderTraversal(root.right, arr)

    def BSTtoMaxHeap(self, root, arr, i):
        if root is None:
            return

        self.BSTtoMaxHeap(root.left, arr, i)
        self.BSTtoMaxHeap(root.right, arr, i)

        i[0] += 1
        root.data = arr[i[0]]

    def convertToMaxHeap(self, root):
        arr = []
        i = [-1]

        self.inorderTraversal(root, arr)
        self.BSTtoMaxHeap(root, arr, i)

    def postorderTraversal(self, root):
        if not root:
            return

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.data, end=" ")
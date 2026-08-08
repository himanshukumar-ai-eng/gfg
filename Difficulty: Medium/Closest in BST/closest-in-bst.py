class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        if root is None:
            return float('inf')

        diff = abs(root.data - k)

        return min(
            diff,
            self.minDiff(root.left, k),
            self.minDiff(root.right, k)
        )
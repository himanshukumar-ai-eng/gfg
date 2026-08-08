class Solution:
    def minDiff(self, root: 'Node', k: int) -> int:
        res = float('inf')
        current = root

        while current is not None:
            res = min(res, abs(current.data - k))

            if current.data > k:
                current = current.left
            else:
                current = current.right

        return res
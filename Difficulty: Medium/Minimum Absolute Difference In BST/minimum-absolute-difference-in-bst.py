class Solution:
    def inorder(self, curr,prev,ans):
        if curr is None:
            return
        self.inorder(curr.left,prev,ans)
        if prev[0] is not None:
            ans[0] = min(ans[0], curr.data - prev[0].data)
        prev[0] = curr
        
        self.inorder(curr.right, prev, ans)
       

    def absolute_diff(self, root):
        prev = [None]
        ans = [float('inf')]

    # inorder traversal (gives sorted order)
        self.inorder(root, prev, ans)

        return ans[0]
        
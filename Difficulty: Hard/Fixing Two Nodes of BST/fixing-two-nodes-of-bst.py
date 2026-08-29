class Solution:
    def correctBST(self, root: 'Node') -> 'Node':
        first = None
        second = None
        prev = None

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)
            if prev and prev.data > node.data:
                if first is None:
                    first = prev
                second = node
            prev = node
            inorder(node.right)
        inorder(root)

        first.data, second.data = second.data, first.data

        return root
            


    

    
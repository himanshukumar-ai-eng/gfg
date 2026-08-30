'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
    def buildTree(self,arr, start, end):
        if start > end:
            return None
        mid = (start + end + 1) // 2
        root = TNode(arr[mid])
        
        root.left = self.buildTree(arr, start, mid - 1)
        root.right = self.buildTree(arr, mid + 1, end)
        return root
    def sortedListToBST(self, head):
        arr = []
        while head:
            arr.append(head.data)
            head = head.next
        return self.buildTree(arr,0,len(arr) - 1)
        
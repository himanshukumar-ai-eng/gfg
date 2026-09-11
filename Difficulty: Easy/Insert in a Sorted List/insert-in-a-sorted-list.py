'''Definition of a Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

class Solution:
    def sortedInsert(self, head, key):
        newNode = Node(key)
        if head is None:
            return newNode
        if key < head.data:
            newNode.next = head
            return newNode
        curr = head
        while curr.next and curr.next.data < key:
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode
        return head
       
        
        
        
        
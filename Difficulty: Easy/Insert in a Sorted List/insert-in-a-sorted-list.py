class Solution:
    def sortedInsert(self, head, key):
        newNode = Node(key)

        # Empty list
        if head is None:
            return newNode

        # Insert at beginning
        if key <= head.data:
            newNode.next = head
            return newNode

        # Find correct position
        curr = head

        while curr.next is not None and curr.next.data < key:
            curr = curr.next

        # Insert new node
        newNode.next = curr.next
        curr.next = newNode

        return head
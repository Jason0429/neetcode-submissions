# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Get length of list
        If length-n-1 < 0 (before the head node) return head.next
        Otherwise iterate until length-n-1 node (Node before the node going to be removed)
        Change that node's next to node.next.next
        Return head
        '''

        def length(node):
            size = 0

            curr = node
            while curr:
                size += 1
                curr = curr.next
            
            return size
        
        size = length(head)

        if size-n-1 == -1:
            return head.next
        
        curr = head
        for _ in range(size-n-1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head

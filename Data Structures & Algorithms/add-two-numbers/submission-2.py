# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        l1 and l2 can be different lengths
        Iterate through each node
        Keep track of ones place and tens place digits
        tens place needs to carry over to the next sum
        If tens != 0 and reached the end, another node necessary that is just the tens place digit
        '''
        
        dummy = ListNode()

        curr1 = l1
        curr2 = l2
        curr = dummy
        tens = 0

        while curr1 and curr2:
            total = curr1.val + curr2.val
            ones = total % 10
            curr.next = ListNode(ones + tens)
            tens = total // 10

            curr1 = curr1.next
            curr2 = curr2.next
            curr = curr.next

        while curr1:
            total = curr1.val + tens
            ones = total % 10
            curr.next = ListNode(ones)
            tens = total // 10

            curr1 = curr1.next
            curr = curr.next

        while curr2:
            total = curr2.val + tens
            ones = total % 10
            curr.next = ListNode(ones)
            tens = total // 10

            curr2 = curr2.next
            curr = curr.next

        if tens > 0:
            curr.next = ListNode(tens)

        return dummy.next
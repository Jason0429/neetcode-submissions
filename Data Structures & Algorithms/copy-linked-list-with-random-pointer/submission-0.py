"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Keep track of dict (Node: next Node)
        Iterate through list and if node not in dict, create it and add to dict
        '''

        node_to_copy = dict()
        dummy = Node(0)

        # copy list without randoms
        curr = head
        curr_copy = dummy
        while curr:
            if curr in node_to_copy:
                curr_copy.next = node_to_copy[curr]
            else:
                node_to_copy[curr] = Node(curr.val)
                curr_copy.next = node_to_copy[curr]

            curr = curr.next
            curr_copy = curr_copy.next

        # add randoms
        curr = head
        curr_copy = dummy.next
        while curr:
            curr_copy.random = node_to_copy[curr.random] if curr.random else None
            curr = curr.next
            curr_copy = curr_copy.next
        
        return dummy.next
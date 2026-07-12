"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = dict()

        def copy(n):
            if not n:
                return None

            if n in old_to_new:
                return old_to_new[n]
            
            new_node = Node(n.val)
            old_to_new[n] = new_node
            new_node.neighbors = [copy(neighbor) for neighbor in n.neighbors]

            return new_node

        return copy(node)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        BST means lesser values are left child, greater values are right child
        Every time we move to the next node, update result with node with minimum value
        '''

        curr = root
        
        while True:
            if p.val < curr.val < q.val or q.val < curr.val < p.val or curr.val in [p.val, q.val]:
                return curr
            
            if p.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
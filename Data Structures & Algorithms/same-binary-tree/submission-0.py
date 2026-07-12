# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        If both p and q are None, return True
        If p.val and q.val are not equal, return False
        If either but not both are None, return False
        Recursively compare isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        '''

        if p is None and q is None:
            return True
        
        if p is None or q is None or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

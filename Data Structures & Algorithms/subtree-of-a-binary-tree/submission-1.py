# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Recursively apply check subroot to each left and right child
        If match, return true
        Return false at the end
        '''

        if subRoot is None:
            return True

        if root is None:
            return False
        
        if self.is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def is_same_tree(self, root, sub_root):
        if root is None and sub_root is None:
            return True
        
        if root is None or sub_root is None:
            return False
        
        if root.val == sub_root.val:
            return self.is_same_tree(root.left, sub_root.left) and self.is_same_tree(root.right, sub_root.right)
        
        return False

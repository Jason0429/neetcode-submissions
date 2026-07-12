# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = [root]

        while q:
            rightmost = None
            q_len = len(q)

            for _ in range(q_len):
                node = q.pop(0)
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightmost:
                res.append(rightmost.val)

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumLeft(node):
            if not node:
                return 0
            s=0
            if node.left and not node.left.right and not node.left.left:
                s+=node.left.val
            s+=sumLeft(node.left)
            s+=sumLeft(node.right)
            return s
        
        return sumLeft(root)
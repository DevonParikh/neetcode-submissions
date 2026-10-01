# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.right and root.left:
                right = 1 + self.maxDepth(root.right)
                left = 1 + self.maxDepth(root.left)
                return max(left,right)
            elif root.left:
                return 1 + self.maxDepth(root.left)
            elif root.right:
                return 1 + self.maxDepth(root.right)
            else:
                return 1
        return 0
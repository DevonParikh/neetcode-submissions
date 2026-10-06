# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxDepth(curr):
            if not curr:
                return 0
            if curr.left and curr.right:
                return 1 + max(maxDepth(curr.left), maxDepth(curr.right))
            elif curr.left:
                return 1 + maxDepth(curr.left)
            elif curr.right:
                return 1 + maxDepth(curr.right)
            return 1

        if not root:
            return True
        if root.left and root.right:
            return -1 <= maxDepth(root.left) - maxDepth(root.right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        elif root.left:
            return maxDepth(root.left) <= 1 and self.isBalanced(root.left)
        elif root.right:
            return maxDepth(root.right) <= 1 and self.isBalanced(root.right)
        return True
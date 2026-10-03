# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Returns height
        def dfs(curr):
            if not curr:
                return 0
            if curr.left and curr.right:
                return 1 + max(dfs(curr.left), dfs(curr.right))
            elif curr.left:
                return 1 + dfs(curr.left)
            elif curr.right:
                return 1 + dfs(curr.right)
            else:
                return 1
        diameter = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                right = dfs(node.right)
            else:
                right = 0
            if node.left:
                stack.append(node.left)
                left = dfs(node.left)
            else:
                left = 0
            if left + right > diameter:
                diameter = left + right
        return diameter
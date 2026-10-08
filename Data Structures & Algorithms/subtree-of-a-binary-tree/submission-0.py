# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == subRoot.val:
                if dfs(curr, subRoot):
                    return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False
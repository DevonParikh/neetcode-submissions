# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            level = level+1
            l = len(q)
            while l > 0:
                element = q.popleft()
                if element.right:
                    q.append(element.right)
                if element.left:
                    q.append(element.left)
                l = l-1
        return level
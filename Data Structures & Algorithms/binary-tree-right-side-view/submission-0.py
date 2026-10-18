# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        q = deque([root])

        while q:
            l = len(q)
            while l > 0:
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                l -= 1
            output.append(curr.val)

        return output
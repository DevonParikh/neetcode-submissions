# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = [[root.val]]
        q = deque([root])
        pos = 0

        while q:
            pos += 1
            l = len(q)
            output.append([])
            while l > 0:
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    output[pos].append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    output[pos].append(curr.right.val)
                l -= 1
        del output[-1]
        return output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []                             # final list of levels
        q = collections.deque([root])       # queue for BFS

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)     # enqueue left child
                    q.append(node.right)    # enqueue right child
            if level:
                res.append(level)           # add current level if not empty

        return res

# Time: O(n)
# Space: O(n)
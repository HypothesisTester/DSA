# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []                         # no nodes → nothing to see

        res = []
        q = collections.deque([root])

        while q:
            level_size = len(q)
            res.append(q[0].val)              # first in queue is the rightmost of this level
            for _ in range(level_size):
                node = q.popleft()
                # enqueue children, right first
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res

# Time: O(n), Space: O(n)
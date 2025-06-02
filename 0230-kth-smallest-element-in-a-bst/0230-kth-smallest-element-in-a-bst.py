# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        # inorder traversal until we find the k-th node
        while cur or stack:
            while cur:
                stack.append(cur)     # go left as far as possible
                cur = cur.left
            
            cur = stack.pop()         # visit node
            n += 1
            if n == k:                # check if it's the k-th
                return cur.val
            cur = cur.right           # then go right
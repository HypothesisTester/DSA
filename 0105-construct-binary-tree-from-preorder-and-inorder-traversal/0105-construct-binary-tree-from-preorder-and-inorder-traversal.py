from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        p = deque(preorder)                          # next root from preorder
        lookup = {v: i for i, v in enumerate(inorder)}  # value → index in inorder

        def rec(start: int, end: int) -> TreeNode:
            if start > end:
                return None                         # no nodes left
            cand = p.popleft()                       # current root value
            root = TreeNode(cand)
            mid = lookup[cand]                       # position in inorder
            root.left = rec(start, mid - 1)          # build left subtree
            root.right = rec(mid + 1, end)           # build right subtree
            return root

        return rec(0, len(preorder) - 1)              # build entire tree

# Time: O(n)
# Space: O(n)
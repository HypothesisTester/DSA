# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None               # reached leaf, not found

        if root.val == val:
            return root               # found the node
        elif root.val > val:
            return self.searchBST(root.left, val)   # go left
        else:
            return self.searchBST(root.right, val)  # go right

# Time: O(h), where h = tree height
# Space: O(h) recursion stack (worst-case h = n for skewed tree)
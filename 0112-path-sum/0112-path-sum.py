# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False                     # no node → no path

        targetSum -= root.val                # subtract current node’s value
        if targetSum == 0 and not root.left and not root.right:
            return True                      # leaf with exact sum

        # recurse left or right
        return (self.hasPathSum(root.left,  targetSum)
             or self.hasPathSum(root.right, targetSum))

# Time: O(n)
# Space: O(h)  (h = tree height)
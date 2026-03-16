# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        max_level = float("-inf")
        arr = []

        def dfs(node, curr_level):
            nonlocal max_level
            if not node:
                return
            
            if curr_level > max_level:
                arr.append(node.val)

            max_level = max(max_level, curr_level)

            dfs(node.right, curr_level + 1)

            dfs(node.left, curr_level + 1)

        dfs(root, 0)
        
        return arr
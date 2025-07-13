# Solution: DFS
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)    
            rh = height(node.right)
            self.max_diameter = max(self.max_diameter, lh + rh)
            return 1 + max(lh, rh)    # height of current subtree

        height(root)
        return self.max_diameter

# Time: O(n) — visits each node once
# Space: O(h) — recursion stack up to tree height h
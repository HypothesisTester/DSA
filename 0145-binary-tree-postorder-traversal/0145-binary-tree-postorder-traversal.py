class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        output = []
        def dfs(node):
            nonlocal output
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            output.append(node.val)
        
        dfs(root)
        return output

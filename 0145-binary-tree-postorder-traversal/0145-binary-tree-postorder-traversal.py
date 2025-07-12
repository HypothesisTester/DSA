# Solution 1: Iteration
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        res.reverse()
        return res

# Time: O(N)
# Space: O(N)

"""
# Solution 2: DFS
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if not node:
                return
            
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        
        postorder(root)
        return res

# Time: O(N)
# Space: O(N)
"""
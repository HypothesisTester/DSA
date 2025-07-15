# Solution 1: DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)   

# Time: O(n) 
# Space: O(n)

"""
# Solution 2: BFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque

        res = 0
        q = deque([(root, root.val)])

        while q:
            node, m = q.popleft()
            if node.val >= m:
                res += 1

            new_max = max(m, node.val)
            if node.left:
                q.append((node.left, new_max))
            if node.right:
                q.append((node.right, new_max))

        return res     

# Time: O(n) 
# Space: O(n) 
"""
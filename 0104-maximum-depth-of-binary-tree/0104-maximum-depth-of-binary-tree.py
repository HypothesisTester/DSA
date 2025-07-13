# Solution 1: Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time: O(N)
# Space: O(H)

"""
# Solution 2: BFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 1
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# Time: O(N)
# Space: O(H)


# Solution 3: Iterative DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            stack = [[root, 1]]
            res = 0

            while stack:
                node, depth = stack.pop()

                if node:
                    res = max(res, depth)
                    stack.append([node.left, depth + 1])
                    stack.append([node.right, depth + 1])
            return res

# Time: O(N)
# Space: O(H)
"""
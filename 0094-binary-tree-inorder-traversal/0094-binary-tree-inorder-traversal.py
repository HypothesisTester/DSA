# Solution 1 Recursive

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []                              # will hold the final inorder sequence

        def inorder(node):
            if not node:
                return                        # base case: null node, return immediately

            # 1) Go as far left as possible before doing anything else
            inorder(node.left)

            # 2) After left subtree is fully processed, append this node’s value
            res.append(node.val)

            # 3) Finally, process the right subtree
            inorder(node.right)

        inorder(root)                         # start the recursion at the root
        return res

# Time: O(n), Space: O(h) where h = tree height

# Explanation of control flow:
# - When `inorder(node)` is called, Python pushes that call onto the stack.
# - It first calls `inorder(node.left)`. That call does the same, going left until node is None.
# - Once it hits `inorder(None)`, that call returns immediately, popping off the stack.
# - Control goes back to the previous `inorder(...)` call, which is now at the line `res.append(node.val)`.
# - After appending, it calls `inorder(node.right)`, repeating the left-then-visit-then-right pattern.
# - Each return “unwinds” the stack by one frame, so after finishing a left subtree, we automatically resume appending the parent’s value.

"""
# Solution 2 Iterative

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []                # result list
        stack = []              # stack for nodes
        cur = root

        # iterate until no nodes left to process
        while cur or stack:
            while cur:
                stack.append(cur)  # push current node and go left
                cur = cur.left
            cur = stack.pop()     # pop leftmost node
            res.append(cur.val)   # visit it
            cur = cur.right       # then explore right subtree
        
        return res

# Time: O(n), Space: O(h) where h = tree height
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)                 # empty spot → create new node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)  # insert into right subtree
        else:
            root.left = self.insertIntoBST(root.left, val)    # insert into left subtree
        return root                                   # return original root

# Time: O(h), Space: O(h)  (h = tree height)

"""

# Solution 2: Iterative
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)                 # empty tree → new root
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)   # attach new node as right child
                    break
                cur = cur.right                 # move right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)    # attach new node as left child
                    break
                cur = cur.left                  # move left
        return root                               # return original root

# Time: O(h), Space: O(1)
"""
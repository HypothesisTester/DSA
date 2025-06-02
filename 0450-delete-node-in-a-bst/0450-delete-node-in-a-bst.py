# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            # 1) The key must be in the right subtree (if it exists)
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # 2) The key must be in the left subtree (if it exists)
            root.left = self.deleteNode(root.left, key)
        else:
            # 3) root.val == key: this is the node to delete!
            if not root.left:
                # Case A: No left child → replace this node with its right child
                return root.right
            elif not root.right:
                # Case B: No right child → replace this node with its left child
                return root.left

            # Case C: Two children exist → find in-order successor
            #    (the smallest node in root.right)
            cur = root.right
            while cur.left:
                cur = cur.left

            # Copy successor's value into this node (‘overwriting’ key).
            root.val = cur.val

            # Delete the duplicate successor from the right subtree:
            # we know successor is root.val, so we remove cur from root.right
            root.right = self.deleteNode(root.right, root.val)

            # return updated subtree root

        return root   

# Time: O(h), Space: O(h)   
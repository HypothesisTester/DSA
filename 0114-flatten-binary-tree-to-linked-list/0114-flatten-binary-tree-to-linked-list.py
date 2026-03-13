class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        arr = []
        
        def preorder(node):
            if not node:
                return
            arr.append(node)          # store the NODE, not node.val
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        
        for i in range(len(arr) - 1):  # -1 to avoid index out of range
            arr[i].left = None
            arr[i].right = arr[i + 1]  # wire to next node in array
        
        arr[-1].left = None            # clean up last node
        arr[-1].right = None
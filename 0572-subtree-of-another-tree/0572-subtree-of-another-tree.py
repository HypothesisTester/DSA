class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:              
            return True
        if not root:                 
            return False

        if self._isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def _isSame(self, s, t):
        if not s and not t:         
            return True
        if not s or not t:      
            return False
        if s.val != t.val:     
            return False

        return (self._isSame(s.left, t.left) and
                self._isSame(s.right, t.right))

# Time: O(m * n) in the worst case, where m = # nodes in root and n = # nodes in subRoot
# Space: O(h), where h is the maximum recursion depth (height of the trees)
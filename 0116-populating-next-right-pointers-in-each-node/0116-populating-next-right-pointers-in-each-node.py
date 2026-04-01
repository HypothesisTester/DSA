"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""



class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        def traverse(level_nodes):
            if not level_nodes:
                return
            
            next_level = []

            for i, node in enumerate(level_nodes):
                if i < len(level_nodes) - 1:
                    node.next = level_nodes[i + 1]
                else:
                    node.next = None

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            traverse(next_level)
        traverse([root])
        return root
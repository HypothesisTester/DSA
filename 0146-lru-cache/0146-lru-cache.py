class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None              # doubly linked
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}           # key → ListNode
        
        self.head = ListNode(-1, -1) # dummy head
        self.tail = ListNode(-1, -1) # dummy tail

        self.head.next = self.tail
        self.tail.prev = self.head

        

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self._remove(node)             # move to MRU position
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node = self.node_map[key]
            self._remove(old_node)
        
        node = ListNode(key, value)
        self.node_map[key] = node
        self._add(node)

        if len(self.node_map) > self.capacity:
            node_to_delete = self.head.next     # least recently used
            self._remove(node_to_delete)
            del self.node_map[node_to_delete.key]

    def _add(self, node):
        # insert node right before tail (MRU position)
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
         # unlink node from its neighbors
         node.prev.next = node.next
         node.next.prev = node.prev

# Time: O(1) for each put() and get() operation
# Space: O(n)
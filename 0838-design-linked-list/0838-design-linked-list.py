class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        # set up empty list with head and tail placeholders
        self.left = ListNode()       
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        # move to the index-th node
        while cur is not self.right and index > 0:
            cur = cur.next
            index -= 1
        # if found and not at tail placeholder, return value
        return cur.val if cur is not self.right and index == 0 else -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        first = self.left.next
        # insert new node before the first real node
        self.left.next = node
        node.prev = self.left
        node.next = first
        first.prev = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        last = self.right.prev
        # insert new node after the last real node
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        # move to the insertion point
        while cur is not self.right and index > 0:
            cur = cur.next
            index -= 1
        # if index is valid, insert before cur
        if index == 0:
            node = ListNode(val)
            prev = cur.prev
            prev.next = node
            node.prev = prev
            node.next = cur
            cur.prev = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        # move to the node to delete
        while cur is not self.right and index > 0:
            cur = cur.next
            index -= 1
        # if valid node, unlink it
        if cur is not self.right and index == 0:
            prev, nxt = cur.prev, cur.next
            prev.next = nxt
            nxt.prev = prev


# Time: O(1), Space: O(1)
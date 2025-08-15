# Solution: Linked List
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)] # dummy node
        

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)     

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        
# Time: O(N / K) for each function call
# Space: O(K + M)
# Where n is the number of keys, k is the size of the set (10000) and m is the number of unique keys
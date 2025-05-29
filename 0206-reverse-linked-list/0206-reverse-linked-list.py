# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None              # will become new head
        curr = head              # start from original head
        
        while curr:              # process until end of list
            nxt = curr.next      # save next node
            curr.next = prev     # reverse current’s pointer
            prev = curr          # advance prev
            curr = nxt           # advance curr
        
        return prev              # prev is new head

# Time: O(n), Space: O(1)
    

# Time: O(n), Space: O(1)

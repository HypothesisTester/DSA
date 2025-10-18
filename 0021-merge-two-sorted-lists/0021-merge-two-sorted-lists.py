# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
 
        dummy = ListNode()
        tail = dummy
        p, q = list1, list2

        while p and q:
            if p.val <= q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next

        tail.next = p or q

        return dummy.next

# Time: O(M+N)
# Space: O(M+N)
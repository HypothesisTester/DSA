# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        preSlow = dummy

        slow = head

        while slow:
            if slow.next and slow.val == slow.next.val:
                fast = slow

                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                
                preSlow.next = fast.next
                
                slow = fast.next

            else:
                preSlow = preSlow.next
                slow = slow.next

        return dummy.next
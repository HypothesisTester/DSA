# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head to simplify edge cases
        dummy = ListNode()
        tail = dummy

        # While both lists have nodes remaining
        while list1 and list2:
            # Pick the smaller head
            if list1.val < list2.val:
                chosen = list1
                list1 = list1.next      # advance in list1
            else:
                chosen = list2
                list2 = list2.next       # advance in list2
        
            tail.next = chosen
            tail = chosen

        # One list is exhausted — append the rest of the other list
        tail.next = list1 or list2

        return dummy.next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases
        if not head or k <= 1:
            return head

        # Dummy to simplify head/tail handling
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # 1. Find the kᵗʰ node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # < k nodes remain; we're done
                    return dummy.next

            group_next = kth.next  # node after this k-group

            # 2. Reverse the k nodes (group_prev.next … kth)
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # 3. Re-attach reversed group
            tmp = group_prev.next    # original head → now tail
            group_prev.next = prev   # prev is new head of this group
            group_prev = tmp         # move group_prev to tail for next round

# Time: O(N)
# Space: O(1)
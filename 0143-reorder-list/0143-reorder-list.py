class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # 1) find middle of list
        mid = end = head
        while end and end.next:
            end = end.next.next
            mid = mid.next

        # 2) reverse second half in-place
        prev, node = None, mid
        while node:
            nxt = node.next
            node.next = prev
            prev, node = node, nxt

        # 3) merge first half and reversed second half
        first, second = head, prev # prev is head of reversed second half
        while second.next:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1      
            first, second = tmp1, tmp2

# Time: O(n) — one pass to find middle, one to reverse, one to merge
# Space: O(1) — in-place node rearrangement only
# Solution: Fast & Slow Pointers
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        # reverse first half while finding mid
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # prev = head of reversed first half; slow = head of second half
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res
        
# Time: O(n)
# Space: O(1)
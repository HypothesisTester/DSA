# Solution: Fast & Slow Pointers
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head
        # find meeting point if cycle exists
        while fast and fast.next:
            slow = slow.next            # +1 step
            fast = fast.next.next       # +2 steps
            if fast == slow:
                # find cycle start
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

# Time: O(n)
# Space: O(1)
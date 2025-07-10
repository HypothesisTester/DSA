# Solution: Iterative
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry: # carry since edgecase 0,0 , carry > 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit 
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

# Time: O(N + M) Where m is the length of l1 and n is the length of l2
# Space: O(1)


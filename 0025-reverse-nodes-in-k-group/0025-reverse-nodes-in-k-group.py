class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
            
        cur = head
        Ktail = None
        new_head = None

        while cur:
            count = 0
            # Store start of current k-group
            temp_head = cur
            
            # Check if we have k nodes
            while count < k and cur:
                cur = cur.next
                count += 1

            if count == k:
                # Reverse k nodes starting from temp_head
                rev_head = self.reverse(temp_head, k)
                
                # Set new_head for first reversed group
                if not new_head:
                    new_head = rev_head
                
                # Connect previous group to current reversed group
                if Ktail:
                    Ktail.next = rev_head

                # Update Ktail to end of current reversed group
                Ktail = temp_head
                # Move head to start of next group
                head = cur
            
        # Connect last reversed group to remaining nodes
        if Ktail:
            Ktail.next = head

        return new_head if new_head else head

    def reverse(self, head, k):
        new_head = None
        prev = head

        while k:
            next_node = prev.next
            prev.next = new_head
            new_head = prev
            prev = next_node
            k -= 1

        return new_head

# Time: O(N)
# Space: O(1)
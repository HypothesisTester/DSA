# Solution 1 Doubly Linked List

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

#Time complexity:
#O(1) time for initialization.
#O(1) time for each visit() function call.
#O(min(n,steps)) time for each back() and forward() function calls.
#Space complexity: O(m∗n)

# Solution 2 Dynamic Array (Optimal)

"""
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.n = 1

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.cur] = url
            self.n = self.cur + 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.n - 1, self.cur + steps)
        return self.history[self.cur] """

#Time complexity:
#O(1) time for initialization.
#O(1) time for each visit() function call.
#O(1) time for each back() and forward() function calls.
#Space complexity: O(m∗n)
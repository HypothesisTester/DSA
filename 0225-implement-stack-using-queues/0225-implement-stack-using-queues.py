class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)                    # enqueue new element

    def pop(self) -> int:
        # rotate front n-1 items to back, then dequeue
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        val = self.pop()                   # remove top
        self.push(val)                     # put it back
        return val

    def empty(self) -> bool:
        return not self.q                  # True if no elements

# Time Complexity:
# __init__: O(1)
# push:    O(1)
# pop:     O(n)
# top:     O(n)
# empty:   O(1)
# Space Complexity: O(n)
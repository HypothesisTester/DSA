class TimeMap:

    def __init__(self):
        self.store = {} #key : list of [list of [val, timestamp]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # default to empty list if key not found
        values = self.store.get(key, []) # get method of dict retrieves the value associated with key

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res

# Time: O(1) for set() and O(log n) for get().
# Space complexity: O(m * n)

"""
Note about accessing values:

So, values is a list where each element is itself a list containing two items:
Index 0: The value (a string, e.g., "bar").
Index 1: The timestamp (an integer, e.g., 1).

For example:

values[0] = ["bar", 1] → values[0][0] = "bar", values[0][1] = 1.
values[1] = ["bar2", 4] → values[1][0] = "bar2", values[1][1] = 4.
"""
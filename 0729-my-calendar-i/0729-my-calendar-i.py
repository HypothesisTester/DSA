class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        l, r = 0, len(self.calendar)

        while l < r:
            mid = (l + r) // 2

            if self.calendar[mid][0] <= startTime:
                l = mid + 1
            else:
                r = mid 

        if self.intersects(l, startTime, endTime):
            return False
        else:
            self.calendar.insert(l, [startTime, endTime])

        return True

    def intersects(self, idx, startTime, endTime):
        return (
            (self.calendar[idx-1][1] > startTime if idx >= 1 else False) or
            (self.calendar[idx][0] < endTime if idx < len(self.calendar) else False)
        )

# Time: O(Log N + O(N)) ==> O(N) 
# Space: O(N)

# Note: Interviewer may ask follow up, how can we improve this? - basically use datastructure where we can insert in log N time, i.e use SortedList in Python which is kind of a linked list behind the scenes
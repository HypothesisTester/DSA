class MedianFinder:

    def __init__(self):
        self.lo = [] # Max heap of low values
        self.hi = [] # Min heap of upper values
        
    def addNum(self, num: int) -> None:
        if len(self.lo) == len(self.hi):
            heapq.heappush(self.hi, -heappushpop(self.lo, -num))
        else:
            heapq.heappush(self.lo, -heappushpop(self.hi, num))
        

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return float(self.hi[0] - self.lo[0]) / 2.0
        else:
            return float(self.hi[0])
            
# Time: O(Log N)
# Space: O(N)

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        val = -heapq.heappushpop(self.small, -num)
        heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        
        return (-self.small[0] + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
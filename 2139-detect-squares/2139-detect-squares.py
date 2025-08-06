class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        x, y = point

        self.points[x][y] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0

        for y2 in self.points[x]:
            delta = abs(y - y2)

            if not delta:
                continue
            
            count += self.points[x][y2]*self.points[x-delta][y2]*self.points[x-delta][y]
            count += self.points[x][y2]*self.points[x+delta][y2]*self.points[x+delta][y]

        return count

# Time: O(1) - add method, O(N) - count method,
# Space: N/A ? , But O(N) ?
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_degrees = minutes * (360/60)
        hour_degrees = (hour * 360/12) + (360/12 * minutes/60)

        diff = abs(minute_degrees - hour_degrees)

        return min(diff, 360 - diff)

# Time: O(1)
# Space: O(1)
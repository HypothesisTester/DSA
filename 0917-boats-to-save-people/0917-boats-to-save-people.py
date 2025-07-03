class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()              # sort by weight
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            # heaviest person at r always gets a boat;
            # if the lightest can join, move l up
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats

# Time: O(n log n) for the sort + O(n) two-pointer scan
# Space: O(1) extra (in-place sort)
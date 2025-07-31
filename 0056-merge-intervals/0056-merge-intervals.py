class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0]) # lamda just define tiny function without giving it a name
        output = [intervals[0]]

        for start, end in intervals[1:]: # intervals[1:] is list slicing, not indexing into the inner list
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

# Time: O(N log N)
# Space: O(N)

            
        
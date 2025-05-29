class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)               # total students waiting
        cnt = Counter(students)           # count of each preference

        for s in sandwiches:             # for each sandwich in stack order
            if cnt[s] > 0:               # if someone prefers this type
                res -= 1                 # they take it
                cnt[s] -= 1              # one less waiting
            else:
                break                    # no one wants this sandwich

        return res

# Time: O(n), Space: O(1)
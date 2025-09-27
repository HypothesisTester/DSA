# Solution: two-pass greedy “balance counter” scan with a string builder
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l_count = r_count = 0

        string_builder = []

        for char in s:
            if char == "(":
                l_count += 1
                string_builder.append(char)
            elif char == ")":
                if l_count > r_count:
                    r_count += 1
                    string_builder.append(char)
            else:
                string_builder.append(char)
        
        if l_count == r_count:
            return "".join(string_builder)
        else:
            res = []

            for i in range(len(string_builder) -1, -1, -1):
                cur_char = string_builder[i]

                if cur_char == "(":
                    if l_count <= r_count:
                        res.append(cur_char)
                    else:
                        l_count -= 1
                elif cur_char == ")":
                    res.append(cur_char)
                else:
                    res.append(cur_char)

            return "".join(reversed(res))

# Time: O(N)
# Space: O(N)
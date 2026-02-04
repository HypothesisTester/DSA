class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            char = strs[0][i]

            for str in strs[1:]:
                if char != str[i]:
                    return strs[0][:i]

        return strs[0][:min_len]
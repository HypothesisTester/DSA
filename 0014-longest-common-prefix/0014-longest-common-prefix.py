class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # find the length of the shortest string
        min_len = min(len(s) for s in strs)
        # build the prefix one character at a time
        for i in range(min_len):
            ch = strs[0][i]
            # compare this character across all strings
            for s in strs[1:]:
                if s[i] != ch:
                    return strs[0][:i]
        # if we never failed, the entire shortest string is the prefix
        return strs[0][:min_len]


# Time: O(N * M)
# Space: O(1) extra (O(M) if you count the output prefix)
        
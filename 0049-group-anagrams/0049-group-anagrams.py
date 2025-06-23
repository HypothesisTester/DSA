from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)         # signature → list of words
        for s in strs:
            count = [0] * 26            # freq of 'a'..'z'
            for c in s:
                count[ord(c) - ord('a')] += 1  # map char → index
            key = tuple(count)         # immutable key for dict
            res[key].append(s)

        return list(res.values())      # convert dict_values → list

# Time: O(N * K) where K = max length of a string
# Space: O(N * K) for counts and output  
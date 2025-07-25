# Solution 1: Dynamic Programming (Top-Down) Using Trie         
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)

        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isWord:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)

# Time: O(N^2 + M*K)
# Space: O(N + M*K)
# Where n is the length of the string s, m is the number of words in the dictionary, and k is the average length of a word in the dictionary.


"""
# Solution 2: Dynamic Programming (Top-Down) Using Hash Set
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words =set(dictionary)
        dp = {}

        def dfs(i):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1) # skip curr char

            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)

# Time: O(N^3 + M*K)
# Space: O(N + M*K)
"""
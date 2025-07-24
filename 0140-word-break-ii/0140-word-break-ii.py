class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def dfs(string: str) -> List[str]:
            if string in memo:
                return memo[string]

            if not string:
                return [""]                       # one empty way to finish

            local_res = []
            for word in wordDict:
                if string.startswith(word):
                    remainder = string[len(word):]
                    sub_sentences = dfs(remainder)

                    for sub in sub_sentences:
                        # only add a space if there *is* a remainder
                        sep = " " if sub else ""
                        local_res.append(word + sep + sub)

            memo[string] = local_res
            return local_res

        # pass s into dfs:
        return dfs(s)
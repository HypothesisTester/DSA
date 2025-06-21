class WordFilter:

    def __init__(self, words: List[str]):
        self.mp = {}                            # "prefix$suffix" → last index
        for i, w in enumerate(words):           # i = word’s index, w = word
            for j in range(len(w)):             # build every non-empty prefix w[0..j]
                pref = w[:j +1]
                for k in range(len(w)):         # build every non-empty suffix w[k..L-1]
                    cur = pref + "$" + w[k:]
                    self.mp[cur] = i            # store every prefix/suffix combo

    def f(self, pref: str, suff: str) -> int:
        key = pref + "$" + suff                 # query key format
        if key not in self.mp:                  # no matching word
            return -1
        return self.mp[key]                      # return stored index


# Time: O(n * m³) init, O(m) per query
# Space: O(n * m³)

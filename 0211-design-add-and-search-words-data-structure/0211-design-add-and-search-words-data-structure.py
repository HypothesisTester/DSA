class TrieNode:
   def __init__(self):
    self.children = {} # a : TrieNode
    self.word = False  # marks end of a valid word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()    # create path
            cur = cur.children[c]
        cur.word = True                         # mark word end
        

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                # Backtracking
                if c == ".":
                    # try all possible next letters
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word                 # true if full match

        return dfs(0, self.root)
        

# Time: addWord = O(m), search = O(m * σ) worst‐case (m = word length, σ = alphabet size)
# Space: O(N) nodes across all words
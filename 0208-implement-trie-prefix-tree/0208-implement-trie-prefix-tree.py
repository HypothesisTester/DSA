class TrieNode:
    def __init__(self):
        self.children = {}      # char → TrieNode
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()    # create path
            cur = cur.children[c]
        cur.endOfWord = True                    # mark word end
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord                     # only true if full word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True                               # prefix exists

# Time: insert/search/startsWith = O(m), m = word length
# Space: O(N) total nodes across all inserts
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
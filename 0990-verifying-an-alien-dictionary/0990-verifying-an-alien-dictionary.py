class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Map each character to its rank in alien alphabet
        orderInd = { c : i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                # If w1 is longer than w2 but shares prefix, not sorted
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    # if w1’s char > w2’s in alien order → not sorted
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False
                    break
        return True

# Time: O(N * M) where N = number of words, M = max word length
# Space: O(1) extra (orderInd is O(1) size)
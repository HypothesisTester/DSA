# Solution Sorting + Hashmap
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True

# Time:  O(n log n) to sort + O(n·groupSize) to build all straights  
# Space: O(n) for the Counter and sort buffer  


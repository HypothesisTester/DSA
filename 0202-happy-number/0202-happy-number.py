# Solution 1: Floyd's Tortoise and Hare Algo

class Solution:
    def isHappy(self, n: int) -> bool:

        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:

            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)

        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output

# Time: O(log n)
# Space: O(1)

"""
# Solution 2: Hash Set
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    
    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10 # modulus
            digit = digit ** 2
            output += digit
            n = n // 10 # int divsion
        return output 

# Time: O(log n)
# Space: O(log n)
"""
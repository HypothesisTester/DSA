# Solution: Stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for token in tokens:
            if token not in operators:
                stack.append(int(token))

                continue

            num2 = stack.pop()
            num1 = stack.pop()

            result = 0

            if token == "+":
                result = num1 + num2
            elif token == "-":
                result = num1 - num2
            elif token == "*":
                result = num1 * num2
            else:
                result = int(num1 / num2) # Rounds correctly for neg values

            stack.append(result)

        return stack.pop()
            
# Time: O(N)
# Space: O(N)

        
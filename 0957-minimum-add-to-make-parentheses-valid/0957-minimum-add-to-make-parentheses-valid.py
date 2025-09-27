# Solution: Balance counter 
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        string_builder = []
        l_count = r_count = m_add = 0

        if not s:
            return 0

        for char in s:
            if char == "(":
                l_count += 1
            elif char == ")":
                if l_count > r_count:
                    r_count += 1
                else:
                    l_count += 1
                    r_count += 1
                    m_add += 1
        
        x = l_count - r_count
        m_add += x
        return m_add

# Time: O(N)
# Space: O(1)

    

        
            

        
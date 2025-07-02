class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        path_items = path.split("/")

        for item in path_items:
            if item == "." or not item: # i.e ////
                continue
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)

# Time: O(N)
# Space: O(N)
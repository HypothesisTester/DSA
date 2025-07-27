class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [num for num in range(numCourses)]

        self.graph = {course: [] for course in range(numCourses)}

        for course, prereq in prerequisites:
            self.graph[course].append(prereq)

        white = set(self.graph.keys())
        grey = set()
        black = set()

        order = []

        while white:
            course = white.pop()

            if course in black:
                continue

            if not self.dfs(course, grey, black, order):
                return []

        return order

    def dfs(self, course, grey, black, order):
        grey.add(course)

        for prereq in self.graph[course]:
            if prereq in black:
                continue

            if prereq in grey:
                return False

            if not self.dfs(prereq, grey, black, order):
                return False

        order.append(course)
        grey.remove(course)
        black.add(course)

        return True
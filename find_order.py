"""
LC 210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses,
return an empty array.
"""


def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = {}
    order = []

    def dfs(node):
        if node in visited:
            if visited[node] == "visiting":
                return False
            return True

        visited[node] = "visiting"
        for nei in graph[node]:
            if not dfs(nei):
                return False
        visited[node] = "done"
        order.append(node)
        return True

    for course in range(numCourses):
        if course not in visited:
            if not dfs(course):
                return []

    return order[::-1]


# Пример

deps = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(find_order(4, deps))

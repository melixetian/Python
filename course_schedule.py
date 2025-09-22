"""
LC 207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    g = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        g[prereq].append(course)

    state = [0] * numCourses

    def dfs(u: int) -> bool:
        if state[u] == 1:
            return False
        if state[u] == 2:
            return True
        state[u] = 1
        for v in g[u]:
            if not dfs(v):
                return False
        state[u] = 2
        return True

    for i in range(numCourses):
        if state[i] == 0:
            if not dfs(i):
                return False

    return True


numCourses = 2
prerequisites = [[1,0],[0,1]]

print(canFinish(numCourses, prerequisites))

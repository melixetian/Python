"""
LC 207. Course Schedule
https://leetcode.com/problems/course-schedule/

Дано numCourses курсов с номерами от 0 до numCourses - 1 и список зависимостей
prerequisites, где prerequisites[i] = [a, b] означает: чтобы пройти курс a,
сначала нужно пройти курс b (ребро b -> a).

Вернуть True, если можно пройти все курсы, иначе False.

Примеры:
    numCourses = 2, prerequisites = [[1, 0]] -> True
    numCourses = 2, prerequisites = [[1, 0], [0, 1]] -> False

Ограничения:
    1 <= numCourses <= 2000
    0 <= len(prerequisites) <= 5000
    prerequisites[i].length == 2
    0 <= a, b < numCourses
    Все пары [a, b] уникальны.
"""

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Топологическая сортировка алгоритмом Кана за O(V + E)."""
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        ready = deque(course for course, degree in enumerate(in_degree) if degree == 0)
        completed = 0
        while ready:
            course = ready.popleft()
            completed += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    ready.append(next_course)

        return completed == numCourses

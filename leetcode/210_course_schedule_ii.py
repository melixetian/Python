"""
LC 210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

Дано numCourses курсов с номерами от 0 до numCourses - 1 и список зависимостей
prerequisites, где prerequisites[i] = [a, b] означает: чтобы пройти курс a,
сначала нужно пройти курс b (ребро b -> a).

Вернуть любой допустимый порядок прохождения всех курсов. Если пройти все курсы
невозможно (в графе есть цикл), вернуть пустой список [].

Примеры:
    numCourses = 2, prerequisites = [[1, 0]] -> [0, 1]
    numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        -> [0, 2, 1, 3] или [0, 1, 2, 3]

Ограничения:
    1 <= numCourses <= 2000
    0 <= len(prerequisites) <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= a, b < numCourses
    a != b
    Все пары [a, b] уникальны.
"""

from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """Топологическая сортировка алгоритмом Кана за O(V + E)."""
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        ready = deque(course for course, degree in enumerate(in_degree) if degree == 0)
        order = []
        while ready:
            course = ready.popleft()
            order.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    ready.append(next_course)

        return order if len(order) == numCourses else []

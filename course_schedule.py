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


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """Поиск цикла в ориентированном графе (DFS в 3 цвета): O(V + E) времени и памяти."""
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 — не посещён, 1 — в текущем пути обхода, 2 — полностью проверен.
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0 and not dfs(course):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))  # True
    print(solution.canFinish(2, [[1, 0], [0, 1]]))  # False

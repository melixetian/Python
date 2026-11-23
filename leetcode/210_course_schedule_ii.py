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


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """Топологическая сортировка через DFS (post-order + разворот): O(V + E) времени и памяти."""
        graph: list[list[int]] = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 — не посещён, 1 — в текущем пути обхода, 2 — полностью проверен.
        state = [0] * numCourses
        order: list[int] = []

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
            order.append(course)
            return True

        for course in range(numCourses):
            if state[course] == 0 and not dfs(course):
                return []

        order.reverse()
        return order


if __name__ == "__main__":
    solution = Solution()
    print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0, 2, 1, 3]
    print(solution.findOrder(2, [[1, 0], [0, 1]]))  # []

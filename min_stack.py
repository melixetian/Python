"""
LC 155. Min Stack
https://leetcode.com/problems/min-stack/

Стек с операциями push, pop, top и getMin за O(1).
Для push и pop на списках Python сложность амортизированная.
Дополнительный стек хранит историю минимумов. Память — O(n).
По условию pop, top и getMin вызываются только для непустого стека.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Повторяющиеся минимумы сохраняем для корректного удаления по одному.
        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())  # -3
    stack.pop()
    print(stack.top())  # 0
    print(stack.getMin())  # -2

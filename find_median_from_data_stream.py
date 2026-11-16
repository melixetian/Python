"""
LC 295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Реализовать класс MedianFinder для последовательного добавления целых чисел
и получения медианы всех добавленных чисел.

Медиана — центральный элемент отсортированной последовательности.
Если элементов чётное количество, медиана равна среднему двух центральных.

Методы:
    addNum(num) — добавить число.
    findMedian() — вернуть текущую медиану.

Пример:
    finder = MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    finder.findMedian()  # 1.5
    finder.addNum(3)
    finder.findMedian()  # 2.0

Ограничения:
    -10**5 <= num <= 10**5.
    До вызова findMedian добавлено хотя бы одно число.
    Всего не более 5 * 10**4 вызовов addNum и findMedian.
"""

from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.lower = []  # Max-куча нижней половины: храним числа со сменой знака.
        self.upper = []  # Min-куча верхней половины: храним исходные числа.

    def addNum(self, num: int) -> None:
        # Сначала добавляем число в нижнюю половину.
        heappush(self.lower, -num)
        # Её максимум переносим в верхнюю, сохраняя порядок между половинами.
        heappush(self.upper, -heappop(self.lower))
        # Нижняя половина должна быть равна верхней по размеру или больше на один.
        if len(self.upper) > len(self.lower):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2

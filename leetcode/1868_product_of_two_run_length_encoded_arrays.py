"""
LC 1868. Product of Two Run-Length Encoded Arrays
https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

Даны два RLE-массива: каждая пара [value, frequency] описывает серию
повторяющихся значений. Вернуть RLE поэлементных произведений,
объединив соседние серии с одинаковым произведением.

Пример:
    encoded1 = [[2, 2], [3, 1]]
    encoded2 = [[3, 2], [2, 1]]
    Результат: [[6, 3]].

По условию частоты положительны, а длины развёрнутых массивов совпадают.
Входные массивы не изменяются и не разворачиваются.
Время — O(n + m), дополнительная память — O(1) без учёта результата.
"""


class Solution:
    def findRLEArray(self, encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
        result = []
        i, j = 0, 0
        remaining1, remaining2 = 0, 0

        while i < len(encoded1) and j < len(encoded2):
            if remaining1 == 0:
                remaining1 = encoded1[i][1]
            if remaining2 == 0:
                remaining2 = encoded2[j][1]

            # Обрабатываем общую часть текущих серий.
            count = min(remaining1, remaining2)
            product = encoded1[i][0] * encoded2[j][0]

            if result and result[-1][0] == product:
                result[-1][1] += count
            else:
                result.append([product, count])

            remaining1 -= count
            remaining2 -= count

            # Указатели продвигаем независимо: обе серии могут закончиться сразу.
            if remaining1 == 0:
                i += 1
            if remaining2 == 0:
                j += 1

        return result

"""
LC 2379. Minimum Recolors to Get K Consecutive Black Blocks
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

У вас есть полоска клетчатой бумаги длины *n*. Каждая клетка либо белая, либо чёрная.
Сколько минимум клеток надо перекрасить из белого цвета в чёрный,
чтобы на полоске существовал отрезок из *k* последовательных клеток чёрного цвета.
Если отрезок из *k* чёрных последовательных клеток уже существует, вернуть 0.
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks.count("W", 0, k)
        best = whites

        for i in range(k, len(blocks)):
            if best == 0:
                break
            if blocks[i - k] == "W":
                whites -= 1
            if blocks[i] == "W":
                whites += 1
            best = min(best, whites)

        return best

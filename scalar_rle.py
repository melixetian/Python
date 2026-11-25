"""
Вычислить скалярное произведение двух RLE-векторов без их разворачивания.
Каждая пара [value, length] задаёт значение и число его повторений.
Частоты должны быть положительными, а длины векторов — одинаковыми.

Пример:
    [[1, 10]] и [[2, 3], [5, 7]]
    Результат: 1 * 2 * 3 + 1 * 5 * 7 = 41.

Функция изменяет частоты во входных списках при частичном расходовании серий.
Время — O(n + m), дополнительная память — O(1).
"""


def scalar_rle(v1: list[list[int]], v2: list[list[int]]) -> int:
    if not v1 and not v2:
        return 0

    len1, len2 = 0, 0
    for _, l in v1:
        if l <= 0:
            raise ValueError("Length should be positive number")
        len1 += l
    for _, l in v2:
        if l <= 0:
            raise ValueError("Length should be positive number")
        len2 += l
    if len1 != len2:
        raise ValueError("Lengths of both vectors should be equal")

    result = 0
    i, j = 0, 0
    while i < len(v1) and j < len(v2):
        subv1, subv2 = v1[i], v2[j]
        l = min(subv1[1], subv2[1])
        result += subv1[0] * subv2[0] * l

        if subv1[1] < subv2[1]:
            i += 1
            subv2[1] -= l
        elif subv1[1] > subv2[1]:
            j += 1
            subv1[1] -= l
        else:
            i += 1
            j += 1

    return result

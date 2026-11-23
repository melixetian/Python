#!/usr/bin/env python3

"""
Дан список целых чисел, повторяющихся элементов в списке нет.
Нужно преобразовать это множество в строку,
сворачивая соседние по числовому ряду числа в диапазоны.

Примеры:
- [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5,8-9,11"
- [1, 4, 3, 2] => "1-4"
- [1, 4] => "1,4"
"""


def compress(lst):
    ans = list()
    srt = sorted(lst)

    i = 0
    while i < len(srt):
        left = srt[i]
        if i == len(srt) - 1:
            ans.append(f"{left}")
            break

        while srt[i + 1] - srt[i] == 1:
            i += 1
            if i == len(srt) - 1:
                break

        right = srt[i]
        if left == right:
            ans.append(f"{left}")
        else:
            ans.append(f"{left}-{right}")
        i += 1

    return ",".join(ans)


res = compress([1, 4, 5, 2, 3, 9, 8, 11, 0])
print(res)

#!/usr/bin/env python3

"""
Реализовать built-in функцию zip(), принимающую набор iterable объектов (I1, I2, ..., In)
и возвращающую кортежи из соответствующих друг другу элементов каждой коллекции:
(I1[0], ..., In[0]), (I1[1], ..., In[1]), ...
Количество кортежей на выходе ограничено длиной самого короткого iterable-аргумента.
При strict=True разная длина аргументов приводит к ValueError.
"""


def my_zip(*objects, strict=False):
    strict = bool(strict)
    iterators = [iter(obj) for obj in objects]

    while iterators:
        items = []
        try:
            for it in iterators:
                items.append(next(it))
        except StopIteration:
            if not strict:
                return

            # Если часть кортежа уже собрана, длины различаются.
            if items:
                raise ValueError("my_zip() arguments have different lengths") from None

            # Первый итератор исчерпан: остальные тоже должны закончиться.
            sentinel = object()
            for it in iterators[1:]:
                if next(it, sentinel) is not sentinel:
                    raise ValueError("my_zip() arguments have different lengths") from None
            return

        yield tuple(items)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5]
    l3 = [3, 4, 5]
    l4 = [5, 4, 3]

    print(*my_zip(l1, l2, l3))
    print(*my_zip(l3, l4))
    print(*my_zip(l1, l2, l3, strict=True))

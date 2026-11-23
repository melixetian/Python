"""
У вас есть полоска клетчатой бумаги длины *n*. Каждая клетка либо белая, либо чёрная.
Сколько минимум клеток надо перекрасить из белого цвета в чёрный,
чтобы на полоске существовал отрезок из *k* последовательных клеток чёрного цвета.
Если отрезок из *k* чёрных последовательных клеток уже существует, то выведите *0*.
"""


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()

        whites = s[:k].count("W")
        best = whites

        for i in range(k, n):
            if best == 0:
                break
            if s[i - k] == "W":
                whites -= 1
            if s[i] == "W":
                whites += 1
            if whites < best:
                best = whites

        print(best)
        print()


if __name__ == "__main__":
    main()

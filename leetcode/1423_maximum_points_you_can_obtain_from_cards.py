def get_card_count(n, k, cards) -> int:
    def rec(deque, value, steps):
        if steps == 0:
            return value
        if steps == 1:
            return max(value + deque[0], value + deque[-1])

        val1 = rec(deque[1:], value + deque[0], steps - 1)
        val2 = rec(deque[:-1], value + deque[-1], steps - 1)
        return max(val1, val2)

    return rec(cards, 0, k)


if __name__ == "__main__":
    """
    n = int(input())
    k = int(input())
    cards = list(map(int, input().split()))
    """
    n = 7
    k = 3
    cards = [5, 8, 2, 1, 3, 4, 11]
    print(get_card_count(n, k, cards))

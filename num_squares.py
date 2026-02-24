"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of
some integer with itself.

For example, 1, 4, 9 and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4
Not coorect: 12 = 9 + 1 + 1 + 1

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9
"""


def solution(n: int) -> int:
    results = [0, 1] + [float("inf")] * n
    squares = [i * i for i in range(1, n)]

    for i in range(1, n + 1):
        for square in squares:
            if square > i:
                break

            results[i] = min(results[i], results[i - square] + 1)

    print(results)

    return results[n]


if __name__ == "__main__":
    print(solution(12))
    print(solution(13))
    print(solution(25))
    print(solution(24))

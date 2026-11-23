#!/usr/bin/env python3

"""
Дан массив из  N целых чисел arr.
Найдите длину максимальной возрастающей подпоследовательности в этом массиве.
"""


def longest_increase(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                print(i, j, dp[i], dp[j], arr[i], arr[j])
                dp[i] = max(dp[i], dp[j] + 1)
                print(dp)
    return max(dp)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(longest_increase(arr))

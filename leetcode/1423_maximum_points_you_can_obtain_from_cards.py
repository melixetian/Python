"""
LC 1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        score = sum(cardPoints[i] for i in range(k))
        best = score

        # Перебираем, сколько из k карт взять с правого конца.
        for from_right in range(1, k + 1):
            score += cardPoints[-from_right] - cardPoints[k - from_right]
            best = max(best, score)

        return best

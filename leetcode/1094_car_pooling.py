"""
LC 1094. Car Pooling
https://leetcode.com/problems/car-pooling/
"""


class Solution:
    def carPooling(self, trips, capacity):
        events = []

        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))

        events.sort(key=lambda x: (x[0], x[1]))

        current = 0
        for _, delta in events:
            current += delta

            if current > capacity:
                return False

        return True

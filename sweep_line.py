"""
You are building a rate-limiting system with a fixed global capacity.
Each request (or job) consumes a certain amount of capacity for a time interval [start, end].
At any point in time, the sum of capacities used by all active requests must not exceed the system limit.
Given a list of requests with their capacity cost and time interval,
determine whether the system can handle all requests without exceeding the limit.

Examples:
Capacity = 10
Requests:
(cost=3, start=1, end=5)
(cost=4, start=2, end=6)
(cost=5, start=4, end=7)
Res: False

Capacity = 10
Requests:
(cost=3, start=1, end=5)
(cost=4, start=2, end=6)
(cost=5, start=6, end=7)
Res: True
"""

START = 0
END = 1


def can_handle(capacity: int, requests: list[tuple[int]]) -> bool:
    events = []

    for cost, start, end in requests:
        if cost > capacity:
            return False

        events.append((start, START, cost))
        events.append((end, END, cost))

    events.sort()

    current = 0

    for _, typ, cost in events:
        if typ == START:
            current += cost
        else:
            current -= cost

        if current > capacity:
            return False

    return True

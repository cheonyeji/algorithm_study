# 2023-08-01 (소요시간 : 30m)
from collections import deque


def solution(people, limit):
    people.sort()
    q = deque(people)

    boat = 0

    while q:
        first = q.popleft()
        boat += 1

        alone = 0
        together = 0
        for i in range(len(q) - 1, -1, -1):
            if q[i] + first > limit:
                alone += 1
            else:
                together += 1
                break

        for i in range(alone):
            q.pop()
            boat += 1

        if together != 0:
            q.pop()

    return boat


print(solution([70, 50, 80, 50], 100))

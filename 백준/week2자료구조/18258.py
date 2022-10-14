# 2022-10-14
# week2 - 자료구조. 큐2
# https://www.acmicpc.net/problem/18258
# 소요시간 : 15:20 ~ 15:30 (10m)

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
commands = [input() for _ in range(N)]

q = deque()
for c in commands:
    if c[0:3] == "pus":
        command, data = c.split(" ")
        q.append(int(data))
    elif c[0:3] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif c[0] == "s":
        print(len(q))
    elif c[0] == "e":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == "f":
        if len(q) == 0:
            print(-1)
        else:
            data = q.popleft()
            print(data)
            q.appendleft(data)
    else:
        if len(q) == 0:
            print(-1)
        else:
            data = q.pop()
            print(data)
            q.append(data)

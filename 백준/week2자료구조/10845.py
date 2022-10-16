# 2022-10-16
# week2 - 자료구조. 큐
# https://www.acmicpc.net/problem/10845
# 소요시간 : 11:35 ~ 11:42 (8m)

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
commands = [input() for _ in range(N)]

dq = deque()
for c in commands:
    if c[0:3] == "pus":
        com, num = c.split(" ")
        dq.append(int(num))
    elif c[0:3] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif c[0] == "s":
        print(len(dq))
    elif c[0] == "e":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == "f":
        if len(dq) == 0:
            print(-1)
        else:
            num = dq.popleft()
            print(num)
            dq.appendleft(num)
    elif c[0] == "b":
        if len(dq) == 0:
            print(-1)
        else:
            num = dq.pop()
            print(num)
            dq.append(num)

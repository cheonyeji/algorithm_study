# 2022-10-16
# week2 - 자료구조. 덱
# https://www.acmicpc.net/problem/10866
# 소요시간 : 12:04 ~ 12:14 (10m)

import sys
from collections import deque

input = sys.stdin.readline

dq = deque()

N = int(input())
commands = [input() for _ in range(N)]

for c in commands:
    if c[0:3] == "pus":
        com, num = c.split(" ")
        if com == "push_front":
            dq.appendleft(int(num))
        else:
            dq.append(int(num))
    elif c[0:3] == "pop":
        if c.replace("\n", "") == "pop_front":
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.popleft())
        else:
            if len(dq) == 0:
                print(-1)
            else:
                print(dq.pop())
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

# 2022-10-10
# week2 - 자료구조. 스택
# https://www.acmicpc.net/problem/10828
# 소요시간 : 23:51 ~ : (m)

import sys

input = sys.stdin.readline

n = int(input())

commands = []
for _ in range(n):
    commands.append(input())

data = []
for c in commands:
    c = c.replace("\n", "")
    if c[0:4] == "push":
        com, val = c.split(" ")
        data.append(int(val))
    elif c == "pop":
        if len(data) == 0:
            print(-1)
        else:
            print(data.pop())
    elif c == "size":
        print(len(data))
    elif c == "empty":
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif c == "top":
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])

# 2022-10-12
# week2 - 자료구조. 에디터
# https://www.acmicpc.net/problem/1406
# 소요시간 : 14:38 ~ 15:24 (50m)

import sys

input = sys.stdin.readline

data = list(map(str, input().replace("\n", "")))
m = int(input())
commands = [input() for _ in range(m)]

pop_data = []
for c in commands:
    if c[0] == "L":
        if len(data) != 0:
            pop_data.append(data.pop())
        else:
            continue
    elif c[0] == "D":
        if len(pop_data) != 0:
            data.append(pop_data.pop())
        else:
            continue
    elif c[0] == "B":
        if len(data) != 0:
            data.pop()
        else:
            continue
    elif c[0] == "P":
        input_c = list(c.split(" "))[1][0]
        data.append(input_c)


print("".join(map(str, data)) + "".join(map(str, pop_data[::-1])))

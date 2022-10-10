# 2022-10-10
# week2 - 자료구조. 괄호
# https://www.acmicpc.net/problem/9012
# 소요시간 : 00:05 ~ 00:18 (15m)

import sys

input = sys.stdin.readline

t = int(input())
data = [input() for _ in range(t)]

for d in data:
    list_d = list(d[:-1])  # 줄바꿈 제거
    flag_vps = True
    vps = 0
    while len(list_d) > 0:
        val = list_d.pop()
        if val == ")":
            vps += 1
        else:
            if vps <= 0:
                flag_vps = False
                break
            else:
                vps -= 1

    if flag_vps and vps == 0:
        print("YES")
    else:
        print("NO")

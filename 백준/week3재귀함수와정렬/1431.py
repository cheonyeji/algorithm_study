# 2022-10-17
# week3 - 재귀함수와 정렬. 시리얼 번호
# https://www.acmicpc.net/problem/1431
# 소요시간 : 17:01 ~ 17:15 (15m)

import sys

input = sys.stdin.readline

N = int(input())
data = [input()[:-1] for _ in range(N)]

num = []

for d in data:
    sum_num = 0
    for val in d:
        if val.isdigit():
            sum_num += int(val)
    num.append((d, len(d), sum_num))

num.sort(key=lambda x: (x[1], x[2], x[0]))

for n in num:
    print(n[0])

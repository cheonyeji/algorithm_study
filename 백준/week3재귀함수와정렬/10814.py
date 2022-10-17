# 2022-10-17
# week3 - 재귀함수와 정렬. 나이순 정렬
# https://www.acmicpc.net/problem/10814
# 소요시간 : 16:44 ~ 16:52 (10m)

import sys

input = sys.stdin.readline

N = int(input())

data = []

for i in range(N):
    age, name = input().replace("\n", "").split(" ")
    data.append((int(age), i, name))

data.sort(key=lambda x: (x[0], x[1]))

for d in data:
    print(d[0], d[2])

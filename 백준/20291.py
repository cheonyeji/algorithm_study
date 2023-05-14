# 2023-05-14
# 백준
# https://www.acmicpc.net/problem/20291
# 소요 시간 : 11:15 ~ 11:27 (12m)

from sys import stdin

input = stdin.readline

d = {}
N = int(input())

for _ in range(N):
    name, extension = input().split(".")
    extension = extension[:-1]
    if extension not in d:
        d[extension] = 1
    else:
        d[extension] += 1

sortedD = sorted(d.items())

for item in sortedD:
    print(item[0], item[1])

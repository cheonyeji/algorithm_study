# 2023-06-07
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/15652
# 소요 시간 : 17:47 ~ 17:49 (5m)

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = []


def dfs(start):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N + 1):
        if i < start:
            continue
        arr.append(i)
        dfs(i)
        arr.pop()


dfs(1)

# 2023-06-07
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/15650
# 소요 시간 : 20m

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = []
isUsed = [False] * (N + 1)


def dfs(start):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if isUsed[i] or i < start:
            continue
        isUsed[i] = True
        arr.append(i)
        dfs(i)
        arr.pop()
        isUsed[i] = False


dfs(1)

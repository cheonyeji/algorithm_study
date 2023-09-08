# 2023-06-07
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/15651
# 소요 시간 : 10m

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = []


def dfs():
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N + 1):
        arr.append(i)
        dfs()
        arr.pop()


dfs()

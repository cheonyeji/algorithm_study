# 2023-09-08 (소요시간 : X 해설봄)
# 백트래킹 [실버3. 백준 15649 N과 M(1)] (https://www.acmicpc.net/problem/15649)

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
arr = []
isUsed = [False] * (N + 1)


def dfs():
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N + 1):
        if isUsed[i]:
            continue
        isUsed[i] = True
        arr.append(i)
        dfs()
        arr.pop()
        isUsed[i] = False


dfs()

# 2023-06-26
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/1182
# 소요 시간 : 16:40 ~ 17:10 (30m)

from sys import stdin

input = stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

arr = []
isUsed = [False] * (N)

answer = 0


def dfs(start):
    global N, S, answer
    if len(arr) != 0 and sum(arr) == S:
        answer += 1

    if len(arr) == N:
        return

    for i in range(N):
        if isUsed[i] or i < start:
            continue
        isUsed[i] = True
        arr.append(data[i])
        dfs(i)
        arr.pop()
        isUsed[i] = False


dfs(0)
print(answer)

"""
TC : 1
5 0
-7 -3 -2 5 8

"""

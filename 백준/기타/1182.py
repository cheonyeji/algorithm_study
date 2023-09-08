# 2023-06-26
# 백준 - 백트래킹
# https://www.acmicpc.net/problem/1182
# 소요 시간 : 16:40 ~ 17:10 (30m)

"""
dfs 함수에 시작한 인덱스를 넘겨주지 않으면 중복허용하는 수열을 생성하게 됨
따라서 시작 인덱스 값을 넘겨줘서 시작인덱스 이전의 데이터는 살펴보지 않도록 해야 조합을 구할 수 있음
"""

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

# 2023-10-02
# 백준 평범한 배낭 https://www.acmicpc.net/problem/12865

from sys import stdin

input = stdin.readline

N, K = map(int, input().split(" "))

data = []
for _ in range(N):
    data.append(list(map(int, input().split(" "))))

max_v = 0


def dfs(start, total_w, total_v):
    global K, max_v
    max_v = max(max_v, total_v)
    for i in range(start + 1, N):
        if total_w + data[i][0] <= K:
            dfs(i, total_w + data[i][0], total_v + data[i][1])


for i in range(N):
    dfs(i, data[i][0], data[i][1])

print(max_v)

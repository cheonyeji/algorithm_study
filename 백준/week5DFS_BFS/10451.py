# 2022-11-02
# week5 - DFS, BFS. 순열 사이클
# https://www.acmicpc.net/problem/10451
# 소요시간 : 00:34 ~ 00:43 (10m)

import sys

input = sys.stdin.readline
from collections import deque


def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split(" ")))

    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        graph[i].append(data[i - 1])

    visited = [False] * (N + 1)

    cycle = 0
    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            cycle += 1

    print(cycle)

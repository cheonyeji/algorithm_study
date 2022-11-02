# 2022-11-02
# week5 - DFS, BFS. 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
# 소요시간 : 23:03 ~ 00:00 (50m)

import sys

input = sys.stdin.readline

from collections import deque


def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = True
                queue.append(y)


N, M = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        bfs(i)

print(cnt)

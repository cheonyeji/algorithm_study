# 2022-11-02
# week5 - DFS, BFS. DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 소요시간 : 20:03 ~ 20:40 (40m)

import sys

input = sys.stdin.readline

N, M, V = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것을 먼저 방문해야 하므로 정렬
for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)


def dfs(start):

    if visited[start]:
        return
    print(start, end=" ")
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)


from collections import deque

queue = deque()


def bfs(start):
    visited[start] = True
    queue.append(start)

    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)

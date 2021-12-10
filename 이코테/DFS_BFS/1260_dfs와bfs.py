# 백준 1260. DFS와 BFS
import sys

input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향 연결

# node 크기가 작은것부터 방문해야 하므로 정렬하기
for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)


def dfs(start):
    visited_dfs[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


dfs(v)
print()
bfs(v)

print(graph)

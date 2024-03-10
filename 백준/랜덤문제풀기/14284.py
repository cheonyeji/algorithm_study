# 2023-10-03
# 백준 간선 이어가기2 https://www.acmicpc.net/problem/14284
# 40m

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split(" "))
visit = [0 for _ in range(n + 1)]


def BFS(start):
    q = deque([start])

    while len(q) > 0:
        node = q.popleft()
        for idx, w in graph[node]:
            if idx != s and (visit[idx] >= visit[node] + w or visit[idx] == 0):
                visit[idx] = visit[node] + w
                q.append(idx)


BFS(s)
print(visit[t])

# def DFS(node):
#     global answer, t
#     if node == t:
#         answer = min(answer, visit[node])
#         return

#     for idx, w in graph[node]:
#         if idx != s and visit[idx] == 0:
#             visit[idx] += visit[node] + w
#             DFS(idx)
#             visit[idx] = 0


# DFS(s)
# print(answer)

# 백준 18352 특정 거리의 도시 찾기
from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

road = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
# distance = [[0] * (n + 1) for _ in range(n + 1)]  # [start][end]
distance = [0] * (n + 1)  # [end]
for i in road:
    graph[i[0]].append(i[1])


def bfs(graph, start):
    q = deque([start])
    distance[start] = 0

    while q:
        v = q.popleft()
        for i in graph[v]:
            # 한번도 방문X
            if distance[i] == 0:
                q.append(i)
                distance[i] = distance[v] + 1


bfs(graph, x)
answer = []

for i in range(1, len(distance)):
    if k == distance[i] and i != x:
        answer.append(i)

answer.sort()

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)

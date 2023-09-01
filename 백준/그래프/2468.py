# 2023-09-01 (소요시간 : 20m)
# 그래프 [실버1. 백준 2468 안전 영역] (https://www.acmicpc.net/problem/2468)

from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline

N = int(input())

max_height = 0
graph = []
for _ in range(N):
    data = list(map(int, input().split(" ")))
    max_height = max(max_height, max(data))
    graph.append(data)

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(i, j, graph, h):
    q = deque([(i, j)])
    # 방문처리
    graph[i][j] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 물에 잠기지 않은 영역일때
                if graph[nr][nc] > h:
                    graph[nr][nc] = 0
                    q.append((nr, nc))


# 아무 지역도 안 잠기는 경우, 안전영역은 전체(1)
safe_area = 1
for h in range(1, 101):
    copy_graph = deepcopy(graph)
    count = 0
    for i in range(N):
        for j in range(N):
            # 물에 잠기지 않은 영역일때
            if copy_graph[i][j] > h:
                bfs(i, j, copy_graph, h)
                count += 1
    safe_area = max(count, safe_area)

print(safe_area)

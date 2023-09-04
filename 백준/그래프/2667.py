# 2023-09-03 (소요시간 : 10m)
# 그래프 [실버1. 백준 2667 단지번호이어붙이기] (https://www.acmicpc.net/problem/2667)

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(sr, sc):
    q = deque([(sr, sc)])
    count = 1
    graph[sr][sc] = 2  # 방문처리
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == "1":
                    count += 1
                    graph[nr][nc] = 2  # 방문처리
                    q.append((nr, nc))
    return count


answer = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == "1":
            answer.append(bfs(r, c))

print(len(answer))
answer.sort()

for num in answer:
    print(num)

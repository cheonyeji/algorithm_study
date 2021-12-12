# 이코테 기출문제 Q16. 연구소
# 백준 12502번 https://www.acmicpc.net/problem/14502
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())  # 행, 열
virus = []  # 바이러스 좌표(row, col)
space = []
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            space.append((i, j))


everyCase = list(combinations(space, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []


def count(graph, n, m):
    answer = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c] == 0:
                answer += 1
    return answer - 3  # 3칸이 세워졌으므로 3빼주기


def goVirus(graph, virus, eachCase):
    temp = copy.deepcopy(graph)
    global n, m, answer
    queue = deque(virus)
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr and nr < n and 0 <= nc and nc < m:
                if temp[nr][nc] == 0 and (nr, nc) not in eachCase:
                    temp[nr][nc] = 2
                    queue.append((nr, nc))

    answer.append(count(temp, n, m))


for eachCase in everyCase:
    goVirus(graph, virus, eachCase)
print(max(answer))

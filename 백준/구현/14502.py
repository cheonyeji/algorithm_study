# 2023-08-23 (소요시간 : 1h)
# 구현 https://www.acmicpc.net/problem/14502

from sys import stdin
import copy
from collections import deque
from itertools import combinations

input = stdin.readline

N, M = map(int, input().split(" "))  # row(y), col(x)

graph = []
blank = []
virus = []

# 입력 받기
for row in range(N):
    data = list(map(int, input().split(" ")))
    for col, d in enumerate(data):
        if d == 0:
            blank.append((row, col))
        if d == 2:
            virus.append((row, col))
    graph.append(data)

dy = [-1, 1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]


def goVirus(map):
    q = deque([])
    for virus_r, virus_c in virus:
        q.append((virus_r, virus_c))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]
            if 0 <= nc < M and 0 <= nr < N:
                if map[nr][nc] == 0:  # 빈칸
                    map[nr][nc] = 2  # 바이러스 전파
                    q.append((nr, nc))  # 새로운 칸 큐에 추가


def countSafe(map):
    result = 0
    for r in range(N):
        for c in range(M):
            if map[r][c] == 0:  # 빈칸이면
                result += 1  # 안전영역 + 1
    return result


result = 0
for comb in combinations(blank, 3):
    # 벽 세우기
    tmp_graph = copy.deepcopy(graph)
    for r, c in comb:
        tmp_graph[r][c] = 1

    goVirus(tmp_graph)
    result = max(result, countSafe(tmp_graph))

print(result)

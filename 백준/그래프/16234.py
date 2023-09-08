# 2023-09-06 (소요시간 : 35m)
# 그래프 [골드4. 백준 16234 인구 이동] (https://www.acmicpc.net/problem/16234)

from sys import stdin
from collections import deque

input = stdin.readline

N, L, R = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(N)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


# 인구이동 발생 여부 return (발생시 True)
def bfs(sr, sc, visit):
    global is_move_ocurred
    move_pos = [(sr, sc)]
    total_ppl = graph[sr][sc]
    q = deque([(sr, sc)])
    visit[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                if L <= abs(graph[r][c] - graph[nr][nc]) <= R:
                    move_pos.append((nr, nc))
                    total_ppl += graph[nr][nc]
                    q.append((nr, nc))
                    visit[nr][nc] = True

    if len(move_pos) != 1:
        is_move_ocurred = True
        num = total_ppl // len(move_pos)
        for r, c in move_pos:
            graph[r][c] = num


day = 0
is_move_ocurred = False
visit = [[False for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            bfs(r, c, visit)

if is_move_ocurred:
    day = 1

while is_move_ocurred:
    is_move_ocurred = False
    visit = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                bfs(r, c, visit)

    if is_move_ocurred:
        day += 1

print(day)

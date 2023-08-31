# 2023-08-31 (소요시간 : 40m)
# 구현 [골드5. 백준 14503 로봇 청소기] (https://www.acmicpc.net/problem/14503)

from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split(" "))  # row : N, col : M
R, C, d = map(int, input().split(" "))

graph = [list(map(int, input().split(" "))) for _ in range(N)]

# d : 0 북 / 1 동 / 2 남 / 3 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def clean(q):
    global N, M, d
    while q:
        r, c = q.popleft()
        # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        if graph[r][c] == 0:
            graph[r][c] = 2

        is_unclean = False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                is_unclean = True
                break
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        if is_unclean:
            d -= 1
            d %= 4
            nr = r + dr[d]
            nc = c + dc[d]

            while graph[nr][nc] != 0:
                d -= 1
                d %= 4
                nr = r + dr[d]
                nc = c + dc[d]
            q.append((nr, nc))

        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        else:
            # 한칸 후진용 임시 방향 temp_d
            temp_d = d
            temp_d += 2
            temp_d %= 4
            nr = r + dr[temp_d]
            nc = c + dc[temp_d]
            # 한 칸 후진할 수 있다면
            if graph[nr][nc] != 1:
                q.append((nr, nc))
            # 뒤쪽 칸이 벽이면 작동 멈추기
            else:
                return


q = deque([(R, C)])
clean(q)

answer = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] == 2:
            answer += 1

print(answer)

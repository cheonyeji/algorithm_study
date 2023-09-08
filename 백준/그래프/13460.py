# 2023-09-06 (소요시간 : 1h 이상 걸려서 해설 참고 )
# 굴러가는 로직이 잘 구현이 안됐다. 무한루프 쓰면 됨
# 그래프 [골드1. 백준 13460 구슬 탈출 2] (https://www.acmicpc.net/problem/13460)

from sys import stdin
from collections import deque

input = stdin.readline

# 목표는 빨간 구슬 구멍으로 빼내기 / 파란 구슬이 들어가면 안됨!
# 공은 동시에 움직인다.
# n = 세로 크기 Row, m = 가로 크기 Col
n, m = map(int, input().split(" "))

# . = 빈칸 / # = 장애물, 벽 / o = 구멍
# 그래프 입력받기
graph = []
R = [0, 0]
B = [0, 0]
target = [0, 0]
for a in range(n):
    sub = list(input())
    graph.append(sub)
    for b in range(m):
        if sub[b] == "R":
            R = [a, b]
        elif sub[b] == "B":
            B = [a, b]
        elif sub[b] == "O":
            target = [a, b]

answer_mark = False

# 상, 하, 좌, 우
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()

# R 좌표, B 좌표
q.append((R[0], R[1], B[0], B[1], 0))

visited = set()
visited.add((R[0], R[1], B[0], B[1]))

while q:
    rx, ry, bx, by, cnt = q.popleft()

    if graph[rx][ry] == "O":
        print(cnt)
        answer_mark = True
        break

    if cnt >= 10:
        continue

    # r, b 움직이기
    for k in range(4):
        r_move = 0
        b_move = 0

        # r 움직이기
        nrx = rx + dx[k]
        nry = ry + dy[k]

        while True:
            # 벽이면 한칸 뒤로 이동
            if graph[nrx][nry] == "#":
                nrx -= dx[k]
                nry -= dy[k]
                break
            elif graph[nrx][nry] == "O":
                break

            nrx += dx[k]
            nry += dy[k]

            r_move += 1

        # b 움직이기
        nbx = bx + dx[k]
        nby = by + dy[k]
        while True:
            # 벽이면 한칸 뒤로 이동
            if graph[nbx][nby] == "#":
                nbx -= dx[k]
                nby -= dy[k]
                break
            elif graph[nbx][nby] == "O":
                break

            nbx += dx[k]
            nby += dy[k]
            b_move += 1

        # B 빠지면 안됨
        if graph[nbx][nby] == "O":
            continue

        # r, b가 같은 경우 / O일때 아닐때
        if nrx == nbx and nry == nby:
            # 더 움직임이 많은걸 한칸 뒤로
            if r_move > b_move:
                nrx -= dx[k]
                nry -= dy[k]
            else:
                nbx -= dx[k]
                nby -= dy[k]

        if not (nrx, nry, nbx, nby) in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, cnt + 1))


if answer_mark == False:
    print(-1)

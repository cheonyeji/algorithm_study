# 2023-10-05
# 1:10 ~ 1:33
# 프로그래머스 거리두기 확인하기 https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque


def bfs(sr, sc, graph):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visit = [[0 for _ in range(5)] for _ in range(5)]

    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                if nr == sr and nc == sc:
                    continue
                if visit[nr][nc] != 0 or graph[nr][nc] == "X":
                    continue
                visit[nr][nc] = visit[r][c] + 1
                if graph[nr][nc] == "P" and visit[nr][nc] <= 2:
                    return False
                q.append((nr, nc))
    return True


def solution(places):
    answer = []

    for idx, place in enumerate(places):
        ppl = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    ppl.append((i, j))
        result = True

        for r, c in ppl:
            if bfs(r, c, place) == False:
                result = False
                break

        if result:
            answer.append(1)
        else:
            answer.append(0)

    return answer

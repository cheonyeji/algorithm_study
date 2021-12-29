# 이코테 DFS BFS Q21 인구이동
# https://www.acmicpc.net/problem/16234
import sys

input = sys.stdin.readline
from collections import deque
import math

# nXn 크기의 땅, 인구 이동 가능 범위 l <= x <= r
N, L, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우 살피기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

day = 0

# 국경선 열기
def openLine(graph, r, c):
    global day
    queue = deque([(r, c)])

    notFriends = []
    friends = [(r, c)]
    sum = graph[r][c]
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]

            if 0 <= nr < N and 0 <= nc < N:
                if L <= abs(graph[row][col] - graph[nr][nc]) <= R:
                    # 인구이동 가능
                    friends.append((nr, nc))
                    sum += graph[nr][nc]
                queue.append((nr, nc))

    day += 1

    # 인구 이동 발생
    num = math.trunc(sum / len(friends))
    for i in friends:
        graph[i[0]][i[1]] = num

    if len(notFriends) != 0:
        # 아직 인구이동이 이루어지지 않은 국가가 있는 경우
        visited = [[False] * (N) for _ in range(N)]
        openLine(graph, notFriends[0][0], notFriends[0][1], visited)
    else:
        # 모두 인구이동이 완료된 경우
        return day


openLine(graph, 0, 0, visited)

# 감시피하기 모든 경우의 수 다 살펴보는 방식으로
from itertools import combinations
import sys

input = sys.stdin.readline
from collections import deque
import copy

n = int(input())
graph = []
teacher = []
space = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append((i, j))
        elif graph[i][j] == "X":
            space.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(teacher):
    queue = deque(teacher)
    temp = copy.deepcopy(graph)
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            row, col = r, c
            while True:
                nx = row + dx[i]
                ny = col + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if temp[nx][ny] == "X":
                        temp[nx][ny] = "T"  # 방문 표시
                    elif temp[nx][ny] == "S":
                        return False  # 학생 찾음
                    elif temp[nx][ny] == "O":
                        break
                    row, col = nx, ny
                else:
                    break

    return True


answer = False
everyCase = list(combinations(space, 3))
for case in everyCase:
    for x, y in case:  # 장애물 세우고
        graph[x][y] = "O"
    if bfs(teacher):
        answer = True
        break
    for x, y in case:  # 원래대로
        graph[x][y] = "X"

if answer:
    print("YES")
else:
    print("NO")

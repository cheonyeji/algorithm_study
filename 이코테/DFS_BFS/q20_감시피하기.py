# # # 이코테 DFS BFS Q20 감시피하기
# # # https://www.acmicpc.net/problem/18428
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
teacher = []
for r in range(n):
    # 자료 입력과 동시에 선생님 위치까지 받을 수 있도록 2중 for문 사용
    graph.append(list(map(str, input().split())))
    for c in range(n):
        if graph[r][c] == "T":
            teacher.append((r, c))

# 좌 우 상 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(teacher):
    global obstacle
    queue = deque(teacher)
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            # 상하좌우 보면서 학생 있나 찾기
            # O가 나오기 전까지 계속 동일 방향 전진 가능
            nr = row + dx[i]
            nc = col + dy[i]
            while (0 <= nr and nr < n and 0 <= nc and nc < n) and graph[nr][nc] != "O":
                if graph[nr][nc] == "S":
                    oldR = nr - dx[i]
                    oldC = nc - dy[i]
                    # 학생 발견 시 바로 전 칸까지만 장애물 설치 가능
                    if graph[oldR][oldC] == "X":

                        graph[oldR][oldC] = "O"
                        obstacle += 1
                        break
                    else:
                        return -1  # -1이 리턴되는 경우, 막을 수 없는 경우임
                # 못 만나면
                else:
                    nr += dx[i]
                    nc += dy[i]
    return obstacle


obstacle = []
bfs(teacher, 0)
if len(obstacle) == 3:
    print("YES")
else:
    print("NO")


def checkRange(r, c):
    global obstacle
    # 범위 입력받아서 해당 범위가 obstacle내에 존재하는지 확인
    for i in range(len(obstacle)):
        for loc in obstacle[i]:
            # 범위 내 존재
            if loc[0][0] <= r <= loc[1][0] and loc[0][1] <= c <= loc[1][1]:
                return i  # 범위 내 존재 O 해당 index에 범위 넣어주기

    return -1  # 범위 내 존재 X, 새로운 index로 obstacle에 삽입


obstacle = [[[(1, 2), (1, 2)], [(3, 4), (3, 4)]], [], []]

for i in range(len(obstacle)):
    for loc in obstacle[i]:
        print(loc[0][0])

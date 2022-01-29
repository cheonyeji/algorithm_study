# 2021-01-29
# 이코테 ch12 구현 문제 Q11 뱀
# https://www.acmicpc.net/problem/3190

from collections import deque

# 보드 크기
n = int(input())

# (1,1)부터 쓰기 위해 n+1 * n+1 크기의 2차원 리스트 선언
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 사과 개수
k = int(input())

for _ in range(k):
    x, y = map(int, input().split())
    # 사과 위치 = 2
    graph[x][y] = 2

# 뱀의 방향 변환 횟수
l = int(input())

second = []
direction = []

for _ in range(l):
    # s=몇초 뒤, d=L(왼쪽90도 방향 회전) / D(오른쪽90도 방향 회전)
    s, d = input().split()
    s = int(s)

    second.append(s)
    direction.append(d)


s = 0  # 초
snake = deque()  # 뱀 저장
hx, hy = 1, 1  # 머리

snake.append((1, 1))

four_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동 남 북 서 방향

d = 0  # 시작할때는 동쪽
leng = 1
graph[hx][hy] = 1

while True:
    hx += four_dir[d][0]
    hy += four_dir[d][1]

    # 만약 그래프 바깥으로 나간 경우 break (벽 꿍)
    if 1 <= hx <= n and 1 <= hy <= n:
        snake.append((hx, hy))  # 머리 다음칸에 위치
        # 사과 O
        if graph[hx][hy] == 2:
            leng += 1  # 몸 길이 1 증가
        # 사과 X & 움직일 수 있는 경우
        elif graph[hx][hy] == 0:
            tx, ty = snake.popleft()
            graph[tx][ty] = 0  # 꼬리 위치 칸 비움
        # 자기 몸이랑 꿍
        else:
            break

        graph[hx][hy] = 1

    else:
        break

    # 이동이 이루어진 뒤 방향을 바꿔야 한다...
    s += 1  # 1초씩 증가
    new_d = ""

    # 방향을 바꿔야하는 경우
    if s in second:
        new_d = direction[second.index(s)]

    # 오른쪽으로 90도 회전
    if new_d == "D":
        d = (d + 1) % 4  # 무작정 빼주면 인덱스 범위가 나가므로 %4해주기
    # 왼쪽으로 90도 회전
    elif new_d == "L":
        d = (d - 1) % 4

print(s + 1)

"""
TC 1 -> 9
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

"""
